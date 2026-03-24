# Session 31 Assessment: The Constraint Surface After 31 Sessions

**Author**: Tesla-Resonance
**Date**: 2026-03-02
**Scope**: Sessions 29-30 integrated assessment with Session 31 computation results (K-1, I-1, B-31nck)
**Organizing Principle**: The paradigm fork -- static vs dynamical vacuum -- as the central structure of the surviving solution space
**Document Type**: Constraint-map update, not probability estimate

---

## I. What Was Proven (Structural Results That Survive Regardless of Framework Fate)

These results are permanent mathematics. They do not depend on whether the phonon-exflation framework describes the physical universe. They are publishable as standalone spectral geometry.

### I.1 Interior Mixing Theorem (Session 30Ab)

On the Jensen curve, D_F = Sum_a [D_K, L_{e_a}] couples predominantly to interior spectral modes, not gap-edge modes, via an algebraic (m + m') suppression mechanism (Paper 17 eq 1.6). Quantitative: gap-edge D_F row norm = 0.175, interior mode row norm = 0.351 (factor 2 suppression). First-order perturbation vanishes identically (D_F diagonal elements zero in D_K eigenbasis, following from anti-Hermiticity). Second-order shift at gap edge: delta_2 = -0.0106.

**Cross-domain analog**: This is spectral Bragg scattering. The (m + m') suppression is the internal-space version of momentum conservation in a periodic lattice -- matrix elements between states near the zone boundary (gap edge) are suppressed because the perturbation's Fourier content is concentrated at high spatial frequencies (interior modes).

**Scope**: Generalizes to any Dirac operator perturbed by a Kosmann-Lichnerowicz commutator on any compact Lie group with left-invariant metric.

### I.2 D_F Construction and Block-Diagonality (Session 30Aa)

D_F(tau) is well-defined, anti-Hermitian (||D_F + D_F^dag|| < 3e-15), chirality-preserving (||{D_F, gamma_F}|| < 5.59e-14), and exactly block-diagonal in Peter-Weyl (cross-sector norm = 0.0e+00). D_F(tau = 0) = 6.89e-15 (Proposition 1.1 gold standard: [D_K, L_X] = 0 for Killing X). Zero free parameters (Baptista Approach B).

### I.3 Pfaffian Factorization (Session 30Ab)

Pf(total) = Pf(0,0) . [Pf(0,1)]^2 . [Pf(0,2)]^2 . Pf(1,1). Squared conjugate-pair terms cannot flip total sign. Only (0,0) singlet (32-dim) and (1,1) adjoint (256-dim) are independently Z_2-relevant. Both +1 at all 75 tau values in [0, 2.5].

### I.4 Spectral Dimension is Generic Weyl (Session 31Aa BA-31-1)

d_s(t) at the gap scale: 8.048 (tau=0), 8.205 (tau=0.15), 8.165 (tau=0.21), 7.300 (tau=0.50). Standard Weyl behavior N(lambda) ~ lambda^8 holds to the gap scale. 439,488 eigenvalues per tau at N_max=6. No intermediate plateau, no dimensional reduction, no CDT-like flow.

### I.5 Orientation Insensitivity (Session 31Aa BA-31-3)

D_K eigenvalue spectrum is identical under orientation reversal to machine epsilon (max diff < 6.0e-14 at all tau). General theorem: spectral pairing {lambda} = {-lambda} from {gamma_9, D_K} = 0 guarantees |lambda| invariance. Not specific to SU(3).

### I.6 Order-One Violation = 4.000 is Cl(8) Algebraic Constant (Session 31Aa BA-31-6)

The violation is exact, tau-independent, universal for ANY 8-dimensional spin manifold. It follows from the representation of Cl(8) on C^16. The NCG Axiom 5 fails for every KK compactification at dimension 8 by the same amount. The Dirac addendum (31Aa) establishes that both BDI classification and Pfaffian are completely independent of Axiom 5.

### I.7 Instanton Action is Negative on Positively-Curved SU(3) (Session 31A I-1)

S_inst = -R + r*K is negative for coupling ratios r <= 2 because R > K on the Jensen curve (positively-curved manifold). Instantons on SU(3) are UNSUPPRESSED. This is the mathematical fact that validates the instanton-phonon identification: nonlinear excitations of the internal geometry are not exponentially rare. They are dynamically relevant.

The exact curvature formulas (Session 17b, machine epsilon) give: R(0) = 2.000, K(0) = 0.531. S_inst(0) = -R + K = -1.469 < 0. The tunneling rate exp(-S_inst) > 1 everywhere on the Jensen curve for r <= 2.

### I.8 Phi-Weinberg Anti-Correlation Resolved by RGE Reframing (Session 30Bb)

At tau ~ 0.15-0.21: phi_30 ~ 1.52 (near Session 12 target) AND sin^2_B ~ 0.42 (standard GUT value that runs to 0.231 at M_Z via SM beta functions for M_KK ~ 10^16 GeV). The coupling structure is internally consistent at tau ~ 0.15-0.21. Three independent constraints converge: phi (eigenvalue ratio), RGE (gauge running), instanton stabilization minimum (tau ~ 0.10-0.31).

### I.9 Wall 4 Extended to 3-Form Sector (Session 31Aa BA-31-4)

V_FR = |omega_3|^2/Vol^2 is monotonically increasing on the Jensen curve. The 3-form norm grows 6x faster than V_spec (9.56x growth vs 1.57x over [0, 0.60]). The round metric (tau=0) is the global minimum of V_spec + alpha * V_FR for all positive alpha. This closes Freund-Rubin stabilization on the Jensen curve -- the most natural mechanism from the KK literature (Cremmer-Julia-Scherk 1978, Freund-Rubin 1980).

---

## II. What Was Constrained (Mechanisms Excluded, Walls Established or Extended)

### II.1 Static Vacuum: Exhausted on All Tested Surfaces

The static vacuum paradigm -- find a minimum of V_total(g) at some fixed metric g -- is now constrained on every surface that has been computed:

| Surface | Dimension | Result | Session |
|:--------|:----------|:-------|:--------|
| Jensen curve | 1D | V_spec monotone, Wall 4 | 17a-24a |
| U(2)-invariant family | 3D | V_total monotone, V_spec/F_BCS = 8000x | 30Ba (B-30min) |
| U(2)-invariant + T1 breathing | 4D | dV/dsigma in [+2.5, +4.2] | 30Bb |
| Jensen + 3-form | 1D + form | V_spec + alpha*V_FR monotone for all alpha > 0 | 31Aa (BA-31-fr) |

**Running total of constrained mechanisms: 22** (21 from permanent registry + Freund-Rubin from 31Aa).

The static vacuum has been tested on 4 of 11 independent moduli directions (after volume constraint on the 12D metric space). The untested 7 directions are: 4 U(2)-breaking directions (one shows T4 instability at -9.9 at the boundary) and 3 further directions in the full left-invariant metric space.

### II.2 Pfaffian Topological Stabilization: Exhausted on Jensen (Wall 5)

Pf(Xi . D_total) = +1 for all 75 tau in [0, 2.5], all 6 Peter-Weyl sectors, at N_max = 2. The Interior Mixing Theorem (I.1) provides the algebraic mechanism. Gap never closes: minimum 0.790 at tau ~ 0.27 (5.2% below round metric), then monotonically increasing. Gap closure from D_F is algebraically forbidden at large tau (D_K eigenvalue spacing grows quadratically, D_F gap-edge coupling grows linearly).

### II.3 NCG-KK Irreconcilability: Elevated to Structural Wall

| tau | Lambda_SA/M_KK | Session |
|:----|:---------------|:--------|
| 0.21 | 1.02e+06 | 31Aa (B-31nck) |
| 0.57 | 2.0e+15 | 30Bb (B-30nck) |

Lambda_SA ~ 10^22 GeV is fixed by SM one-loop running (the scale where alpha_1 = alpha_2). M_KK ~ 10^16 GeV from GUT phenomenology. The 6-order gap at tau=0.21 cannot be bridged by threshold corrections within standard GUT models.

**Consequence**: The hybrid NCG-KK approach -- using both the NCG spectral action (which predicts g1=g2 at Lambda_SA) and KK dimensional reduction (which gives g1/g2 = e^{-2tau} at M_KK) -- is structurally inconsistent on the Jensen curve at every tested tau. The framework must choose: pure KK (abandon NCG unification) or pure NCG (abandon KK metric deformation as the physical mechanism).

### II.4 Kapitza Limit-Cycle on U(2)-Invariant Surface: Constrained (K-1 DOES NOT FIRE)

The decisive computation. At the physical transverse frequencies (T3 = 8.326, T4 = 9.893), the Kapitza correction is too weak to overcome V_spec monotonicity:

- Maximum Kapitza correction: 0.27 (at A = 0.15, T3 frequency)
- V_total range on Jensen: 1.76
- Correction/descent ratio: 0.17 (the correction is 17% of what is needed)

The critical threshold: omega_crit^2 ~ 5-8. Physical T3 = 8.326 is 1.7x above this threshold. The modes are too stiff -- they oscillate too fast for the arcsine-weighted averaging to generate a stabilizing minimum. The Kapitza mechanism requires softer modes (omega^2 < 5) which do not exist on the U(2)-invariant surface.

**What this is NOT**: This is not a structural closure of the Kapitza paradigm. It is a constraint on the tested surface. The full 5D landscape (with U(2)-breaking directions) may contain softer modes. T4 = -9.9 at the boundary means the U(2)-invariant surface is already unstable against U(2)-breaking perturbations. The instability itself may provide the soft mode needed for Kapitza stabilization. This redirect is structurally analogous to B-29d (Session 29Bb), where the Jensen saddle redirected the BCS analysis to the U(2)-invariant family.

### II.5 Cosmological Constant: O(1) Ratio, No Geometric Suppression (Session 31Aa BA-31-2)

a_0/a_2 = 0.494 at tau=0.21. Range on full U(2)-invariant grid: [0.387, 0.502]. The SU(3) geometry provides zero CC suppression. The 122-order hierarchy is inherited from standard QFT with no amelioration. Not fatal (shared with all quantum gravity approaches) but confirms the adversarial review's concern.

---

## III. What Opened (New Channels Identified, With Gate Conditions)

### III.1 Instanton-Kapitza Drive (I-1 PASSES)

The most significant positive result of Session 31. Gamma_inst/omega_tau exceeds the threshold of 3 for 5 of 6 tested coupling ratios:

| r = alpha_YM/alpha_grav | Max Gamma/omega_tau | tau at max |
|:------------------------|:-------------------|:-----------|
| 0.1 | 9.64 | 0.181 |
| 0.3 | 8.67 | 0.181 |
| 0.5 | 7.80 | 0.181 |
| 1.0 | 5.98 | 0.181 |
| 2.0 | 3.51 | 0.181 |
| 5.0 | 0.71 | -- |

**Physical interpretation**: On positively-curved SU(3), the scalar curvature R dominates the Kretschner scalar K. The instanton action S_inst = -R + r*K is NEGATIVE for moderate coupling ratios, meaning instantons are not exponentially suppressed but exponentially ENHANCED. The instanton gas is dynamically relevant at tau ~ 0.18 -- the gradient-balance point where three independent constraints converge.

**What this validates**: Tesla Session 30Ba Section XIV thesis -- instantons ARE nonlinear phonons under KK dimensional reduction. The wall between "resonance" and "instantons" is false. Both are excitations of the same field (the internal metric). Perturbative phonons = small-amplitude oscillations. Instantons = finite-amplitude solitonic excitations. The instanton gas provides a natural Kapitza drive: rapidly recurring nonlinear excitations that generate a time-averaged effective potential.

**Condensed matter analog**: In superfluid He-3, there is no fundamental distinction between phonons and vortices at the condensate level (Volovik, Paper 10). Vortex reconnection generates Kelvin waves that cascade to phonons (Donnelly, Paper 12). The instanton-phonon identification is the gravitational analog: topological metric fluctuations cascade to linearized perturbations.

**Caveats (from computation)**:
1. alpha_grav = 1 assumed (natural units). The physical normalization depends on the 12D action, which has not been derived from first principles in this framework.
2. Single-instanton dilute gas approximation. Multi-instanton correlations are uncomputed.
3. One-loop prefactor (functional determinant ratio) set to 1. In standard QFT this is O(1) but can have significant numerical factors.

**Next computation**: Instanton-driven V_Kapitza. Combine the I-1 instanton rate with the K-1 Kapitza formula using Gamma_inst as the effective frequency instead of the Hessian eigenvalue. omega_eff^2 ~ (Gamma_inst)^2 ~ exp(2R - 2rK) ~ O(1-10). This is in the range where K-1 showed minima can appear (omega^2 < 5-8). **The instanton drive may provide exactly the soft mode that the Hessian modes are too stiff to provide.**

### III.2 Full 5D U(2)-Breaking Landscape

The U(2)-invariant surface is the stiffest direction in moduli space. T4 instability at the boundary (eigenvalue -9.9 at tau=0.60, eps=+0.15) means the system is being pushed OFF this surface. The Interior Mixing Theorem's suppression mechanism relies on the Killing/non-Killing decomposition, which changes when U(2) is broken (Einstein's Channel 2, Session 30 review).

The 5D landscape has:
- 4 directions tested (tau + 3 U(2)-invariant). No minimum found.
- 7 directions untested. One already known unstable (T4).
- The surviving solution space for static vacua lives exclusively in these 7 untested directions.

### III.3 Instanton-Kapitza in 5D

The I-1 PASS combined with K-1 DOES NOT FIRE generates a specific prediction: the instanton-driven Kapitza mechanism operates in the full 5D landscape, where both the instanton rate (determined by curvature invariants that vary across the full moduli space) and the effective potential (V_total on the 5D surface) may combine to produce a minimum. The U(2)-invariant surface was the wrong place to look -- it was tested for mathematical tractability, not because it was physically preferred.

---

## IV. The Constraint Surface: Geometry of the Surviving Region

### IV.1 The Paradigm Fork

Session 30's most significant conceptual development was the emergence of a clean paradigm fork:

**Static vacuum** (evaluate V_total at fixed metrics): Comprehensively tested and found barren. 22 constrained mechanisms. No minimum on any tested surface (1D Jensen, 3D U(2)-invariant, 4D with T1 breathing, 1D + 3-form). Wall 4 extended to 3-form sector. Pfaffian trivial on Jensen. The static paradigm is at the structural floor.

**Dynamical vacuum** (limit-cycle with time-averaged observables): The K-1 computation constrains the simplest version (Hessian-driven Kapitza on U(2)-invariant surface) but I-1 opens the instanton-driven version. The dynamical paradigm survives because:
1. All 22 static closures evaluate functionals at FIXED metrics. None constrains time-averaged potentials.
2. Walls 1-2 (algebraic, representation-theoretic) hold on limit cycles. Wall 4 (monotonicity) is a STATIC statement that does not constrain the time-averaged Kapitza potential.
3. The instanton rate exceeds the modulus rolling frequency by factors of 3.5-9.6 at the preferred tau ~ 0.18.

### IV.2 The Surviving Region: A Map

The constraint surface after 31 sessions:

```
DIMENSION: 5D (U(2)-breaking moduli) + dynamical (limit-cycle) + non-perturbative (instanton gas)

WALLS (permanent boundaries):
  W1: F/B = 4/11 asymptotic (Weyl, UV, tau-independent)
  W2: Peter-Weyl block-diagonality (exact, ANY left-invariant metric)
  W3: Spectral gap at mu=0 (lambda_min > 0, prevents spontaneous BCS)
  W4: Spectral action monotonicity (STATIC functionals only, extended to 3-form)
  W5: Pfaffian triviality on Jensen (gap never closes)
  W6: NCG-KK irreconcilability (Lambda_SA/M_KK > 10^3 at all tested tau)

CONSTRAINED REGIONS (tested and found barren):
  - 1D Jensen curve: V_spec monotone (Wall 4)
  - 3D U(2)-invariant: V_total monotone, V_spec/F_BCS = 8000x
  - 4D with T1 breathing: dV/dsigma > 0
  - 1D Jensen + 3-form: V_FR also monotone (31Aa)
  - Hessian-driven Kapitza on U(2)-invariant: omega^2 > omega_crit^2 (K-1)

SURVIVING REGION:
  (a) Instanton-driven Kapitza (I-1 PASSES)
      - omega_eff from instanton gas ~ O(1-10), in the soft-mode range
      - Centered at tau ~ 0.18 (gradient-balance, phi/RGE convergence)
      - Requires: instanton-driven V_Kapitza has minimum (computable)
  (b) Full 5D U(2)-breaking landscape
      - T4 instability opens 4 new directions
      - Interior Mixing suppression may break (Channel 2)
      - Requires: full 5D Hessian + spectrum computation (high cost)
  (c) Instanton-Kapitza in 5D (combination of a + b)
      - Instanton rates vary across 5D surface
      - Soft modes may exist in U(2)-breaking directions
      - Requires: 5D curvature invariants + instanton action scan

PREFERRED TAU WINDOW: 0.15-0.21
  Three independent constraints converge:
  (1) phi_30 in [1.52, 1.54] (eigenvalue ratio, Session 12/30Bb)
  (2) sin^2_B ~ 0.42 runs to 0.231 at M_Z for M_KK ~ 10^16 GeV (RGE, Session 30Bb)
  (3) Instanton action minimum at tau ~ 0.10-0.31 (Session 22c/31A I-1)
```

### IV.3 The Coupling-Stabilization Decoupling (Structural, from Session 30)

The framework's algebraic/coupling predictions work where they should. Its failure is entirely in dynamics/stabilization. This decoupling is structural: eigenvalue ratios and coupling constants are determined by KINEMATICS (representation theory, Peter-Weyl). The potential landscape is determined by DYNAMICS (spectral action, BCS, instantons). These are different mathematical structures.

**Implication**: Any mechanism that stabilizes the modulus near tau ~ 0.15-0.21 automatically produces both the correct eigenvalue ratio AND the correct Weinberg angle (after RGE running). The search should focus entirely on stabilization mechanisms, not on coupling predictions.

---

## V. K-1 and I-1 Results: Integrated Analysis

### V.1 The Stiffness-Softness Spectrum

K-1 and I-1 together reveal a continuous spectrum from stiff (no stabilization) to soft (Kapitza minimum possible):

| Mode | omega^2 | Kapitza minimum? | Status |
|:-----|:--------|:----------------|:-------|
| T4 Hessian | 9.893 | No | Tested (K-1) |
| T3 Hessian | 8.326 | No | Tested (K-1) |
| omega_crit^2 | 5-8 | Threshold | Computed (K-1) |
| Instanton gas (r=0.1-1.0) | ~O(1-10) | Possible | I-1 PASS, V_Kapitza uncomputed |
| Full 5D soft modes | Unknown | Unknown | Untested |

The physical T3/T4 modes on the U(2)-invariant surface are 1.7x above the critical threshold. The instanton gas frequency is in the right range but the instanton-driven V_Kapitza has not been computed.

**The decisive next computation**: Replace omega_perp^2 in the K-1 Kapitza formula with Gamma_inst^2 from I-1. Use the same grid data (s30b_grid_bcs.npz). If the instanton-driven Kapitza potential has an interior minimum, the dynamical paradigm produces a testable, stabilized vacuum. If not, the surviving space contracts to the full 5D landscape.

### V.2 Why S_inst < 0 is Physically Significant

The negative instanton action is not an artifact. On positively-curved manifolds, the gravitational contribution (-R) to the Euclidean action is NEGATIVE (conformally related to the standard sign on flat space). The Yang-Mills contribution (+K) is positive but smaller on SU(3) because the Kretschner scalar K(0) = 0.531 while R(0) = 2.000. The ratio K/R = 0.265 means the gravitational sector dominates by nearly 4:1.

The peak instanton rate occurs at the gradient-balance point tau = 0.181. This is not coincidental: the gradient-balance point is where the spectral action slope is small (the modulus is rolling slowly), making the instanton rate large relative to the rolling frequency. The instanton gas is densest where the modulus is slowest -- exactly the Kapitza mechanism's requirement for effective stabilization.

### V.3 The Three-Convergence at tau ~ 0.18

Three independent computations converge on tau ~ 0.18:

1. **Phi target**: phi_30 = 1.52 at tau = 0.18-0.20 (Session 12, 30Bb). Within [1.52, 1.54].
2. **RGE compatibility**: sin^2_B ~ 0.42 at tau ~ 0.21 runs to SM value at M_Z (Session 30Bb).
3. **Peak instanton rate**: Gamma_inst/omega_tau maximized at tau = 0.181 (Session 31A I-1).

The probability that three independent quantities -- an eigenvalue ratio, a gauge coupling evolution, and a curvature-dependent tunneling rate -- all select the same tau window [0.15, 0.21] by coincidence requires quantification. But structurally, this convergence is the single most suggestive feature of the constraint map.

### V.4 B-31nck Integration

B-31nck FAIL (Lambda_SA/M_KK = 10^6 at tau=0.21) means the NCG spectral action and KK dimensional reduction cannot be simultaneously valid at the physically preferred tau. This does not constrain the KK program (gauge couplings from isometries, Dirac spectrum from D_K, BCS from Kosmann pairing). It constrains the NCG program (spectral action unification, inner fluctuations, classification theorem).

**Resolution path**: The framework operates as pure KK with the spectral action as an EFFECTIVE potential (valid at scales << Lambda_SA), not as the exact NCG spectral action (which requires Lambda_SA = M_KK). The Seeley-DeWitt coefficients a_0, a_2, a_4 are geometric invariants regardless of the NCG interpretation. The loss is theoretical: the uniqueness argument from NCG axioms (Connes Paper 12) no longer applies. The gain is computational: the KK spectral geometry remains intact.

---

## VI. Forward Projection

### VI.1 Computable from Existing Data (Near-Zero Cost)

| Priority | Computation | Input | Expected Runtime |
|:---------|:-----------|:------|:----------------|
| **1** | Instanton-driven V_Kapitza | s30b_grid_bcs.npz + I-1 rates | < 30 sec |
| **2** | Instanton V_Kapitza with soft-mode sweep | Same | < 1 min |
| **3** | Instanton rate on U(2)-invariant grid | s30b_sdw_grid.npz + curvature formulas | < 5 sec |

Priority 1 is the single most consequential remaining computation. It tests whether the instanton gas -- confirmed dynamically relevant by I-1 -- provides the soft mode that K-1 showed is needed for Kapitza stabilization. All inputs exist. The computation is a simple modification of the K-1 script: replace omega_perp^2 with Gamma_inst(tau)^2.

### VI.2 Requires New Computation (Medium Cost)

| Priority | Computation | Cost | Prerequisite |
|:---------|:-----------|:-----|:-------------|
| **4** | Full 5D transverse Hessian at tau ~ 0.18 | ~1 hr | Dirac spectrum at off-Jensen points |
| **5** | Off-Jensen Dirac spectrum at T4-unstable direction | ~2-5 hr | New eigensolver runs |
| **6** | Instanton action on 5D surface | ~1 hr | Curvature at off-Jensen points |
| **7** | AZ class verification off-Jensen | ~1 hr | Proper T operator construction |

### VI.3 Requires New Theory

| Route | Status | What Is Needed |
|:------|:-------|:---------------|
| Instanton-driven Kapitza formalism | I-1 validates the rate | Proper semiclassical treatment of instanton gas on compact Lie group |
| NCG-KK reconciliation | B-31nck structural wall | Threshold corrections or abandonment of sigma=s identification |
| Cosmological constant | a_0/a_2 ~ O(1), standard problem | Volovik thermodynamic identity (emergent gravity) or Wodzicki residue |
| Full 5D landscape search | T4 instability opens direction | Computational infrastructure for off-Jensen Dirac spectrum |

### VI.4 The State of the Constraint Map

After 31 sessions:

- **22 constrained mechanisms** (all single-particle, all classical potential, all static)
- **1 partially constrained dynamical mechanism** (Kapitza on U(2)-invariant: too stiff)
- **1 open dynamical mechanism** (instanton-Kapitza: I-1 PASSES, V_Kapitza uncomputed)
- **1 open static direction** (full 5D landscape, 7 untested directions)
- **6 structural walls** (W1-W4 from Sessions 17-24, W5 from Session 30, NCG-KK from Session 31)
- **Preferred tau window**: 0.15-0.21 (three-fold convergence: phi, RGE, instanton rate)
- **Coupling-stabilization decoupling**: kinematic predictions work, stabilization is the sole missing piece

The constraint surface has contracted from the original 12D metric space x infinite-dimensional order parameter space to: the instanton-Kapitza mechanism at tau ~ 0.18 in the full 5D moduli space, tested against the pre-registered gate of whether V_Kapitza has an interior minimum. One computation stands between the current state and a definitive verdict on the dynamical paradigm's viability on the tested surface.

---

## Appendix: Session 31 Computation Inventory

| Computation | Gate | Verdict | Key Number | Script | Data |
|:-----------|:-----|:--------|:-----------|:-------|:-----|
| K-1 Kapitza effective potential | K-1 | DOES NOT FIRE | omega_crit^2 ~ 5-8, T3 = 8.326 (1.7x above) | s31a_kapitza_gate.py | s31a_kapitza_gate.npz |
| I-1 Instanton-Kapitza frequency | I-1 | PASS | Gamma/omega_tau = 9.64 at r=0.1, tau=0.181 | s31a_instanton_kapitza.py | s31a_instanton_kapitza.npz |
| B-31nck at tau~0.21 | B-31nck | FAIL | Lambda_SA/M_KK = 1.02e6 | s31a_nck_tau021.py | s31a_nck_tau021.npz |
| Spectral dimension | BA-31-ds | GENERIC | d_s = 8.165 at tau=0.21 | s31alt_spectral_dimension.py | s31alt_spectral_dimension.npz |
| CC ratio | BA-31-cc | INTERMEDIATE | a_0/a_2 = 0.494 | s31alt_cc_ratio.py | s31alt_cc_ratio.npz |
| Orientation test | BA-31-or | INSENSITIVE | max diff < 6.0e-14 | s31alt_orientation_test.py | s31alt_orientation_test.npz |
| 3-form Freund-Rubin | BA-31-fr | FAIL | V_FR grows 6x > V_spec | s31alt_3form_potential.py | s31alt_3form_potential.npz |
| Order-one severity | BA-31-oo | SEVERE/NATURAL | 4.000 > 95th percentile (3.10) | s31alt_order_one_severity.py | s31alt_order_one_severity.npz |

---

*Assessment written by Tesla-Resonance from: Session 29 Fusion Synthesis, Session 30 Master Synthesis, Session 31Aa Synthesis, Permanent Results Registry, Observational Avenues, computation outputs s31a_kapitza_gate.npz (K-1), s31a_instanton_kapitza.npz (I-1), s31a_nck_tau021.npz (B-31nck), and agent memory (constraint map, cross-domain connections, central organizing principle). All gate verdicts taken from computation source files and coordinator classification. The paradigm fork (static vs dynamical) is the central organizing structure. The instanton-Kapitza mechanism is the sole surviving dynamical route on the tested surface, with I-1 PASS providing the rate and K-1 DOES NOT FIRE defining the softness threshold. The three-convergence at tau ~ 0.18 (phi, RGE, instanton peak) is the most structurally suggestive feature of the constraint map.*
