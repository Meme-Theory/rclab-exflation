# Session 28 Team Synthesis C: Neutrino / Condensed Matter / Mass Quantization

**Date**: 2026-02-27
**Team**: Neutrino (neutrino-detection-specialist), Landau (landau-condensed-matter-theorist), Paasch (paasch-mass-quantization-analyst), Coordinator
**Process**: 3-round deliberation (cross-domain considerations -> refined assessments -> targeted disagreement resolution)
**Input files**: session-28-neutrino-collab.md, session-28-landau-collab.md, session-28-paasch-collab.md

---

## I. Executive Summary

Three specialists assessed Session 28 results from complementary domains: neutrino mass phenomenology, condensed matter phase transition theory, and mass quantization analysis. The deliberation produced five consensus findings, one critical new result, one honest downgrade, and a prioritized Session 29 diagnostic list.

**Central finding**: R_BCS = R_bare at leading order (uniform intra-sector gap cancels in mass-squared ratios). The BCS condensate does NOT rescue the neutrino mass ratio failure (R = 5.68, gate [17,66]). A mode-dependent gap correction exists from the tridiagonal Kosmann kernel but likely pushes R in the wrong direction. The neutrino program's last remaining test is tridiagonal PMNS extraction (mixing angles).

**Key downgrade**: phi_paasch at tau=0.15 reclassified from "physical prediction" to "mathematical property of the D_K spectrum" -- the BCS interior minimum sits at tau=0.35 where the ratio drifts 5% from phi_paasch. Evidential weight reduced from BF=5 to BF=2 (marginal).

**Key upgrade**: L-9 first-order character upgraded from "neutral Landau classification" to "structurally necessary for the clock constraint" -- without discontinuous freeze, continuous tau_dot violates atomic clock bounds by 15,000x.

---

## II. Consensus Findings (All 3 Specialists Agree)

### II.1 Tridiagonal Selection Rules Are a Three-Way Convergence

The strongest structural result of the deliberation. The Session 23a selection rules -- V(L1,L2) = 0.07-0.13, V(L1,L3) = 0 exactly, V(L2,L3) = 0.01-0.03 -- simultaneously explain three independent phenomena:

| Domain | Consequence | Mechanism |
|:-------|:-----------|:----------|
| Neutrino (PMNS) | theta_12 >> theta_13 mixing hierarchy | Tridiagonal mass matrix eigenvectors |
| Paasch (mass quantization) | phi_paasch^1 survives but phi_paasch^n does not | Nearest-neighbor tight-binding: only adjacent levels coupled |
| Landau (BCS/d_eff) | Effective hopping structure for order parameter | Tridiagonal Kosmann kernel determines inter-mode coupling |

**Origin** (Paasch, Round 2): The V(L1,L3)=0 selection rule arises from the angular momentum triangle inequality on SU(3). The pairing matrix element V_{nm} involves an integral over SU(3) of three Dirac eigenfunctions, and the triangle inequality on (p,q) quantum numbers forces coupling to zero when sectors are too far apart in the Peter-Weyl lattice. This is one algebraic identity with three physical consequences.

**Status**: PERMANENT. Algebraic origin (SU(3) representation theory), not geometric (Jensen metric). Robust under all deformations that preserve SU(3) structure.

### II.2 L-9 First-Order Character Is Structurally Necessary

The cubic invariant c = 0.006-0.007 in (3,0)/(0,3) sectors (Session 28b L-9) is not merely a Landau classification result -- it is REQUIRED by the atomic clock constraint (Session 22d E-3).

**Argument** (Neutrino Round 1, Landau Round 2 confirmation):
- Clock constraint: |dalpha/alpha| = 3.08 * |tau_dot| < 10^{-16}/yr requires tau_dot = 0 to 25 ppm
- Second-order transition: tau_dot approaches zero as t^{-beta/(z*nu)} -- asymptotic, never reaches zero in finite time (critical slowing down)
- First-order transition: Delta jumps discontinuously from 0 to Delta_0, condensation energy creates instantaneous potential barrier, tau_dot jumps to zero (or exponentially suppressed value)
- Therefore: first-order character is NECESSARY, not merely consistent

**Upgrade**: L-9 moves from NEUTRAL to STRUCTURALLY NECESSARY in the Constraint Chain assessment.

### II.3 BEC-Side Crossover Partially Rescues phi_paasch Through Condensation

**Background**: Paasch proved in Session 27 that weak-coupling BCS (Delta ~ exp(-1/M)) destroys phi_paasch structure in gap ratios (amplified to 64,354 at tau=0.15).

**Landau's BEC-side reframing** (Round 1, confirmed Round 2): f_0 = -300 places the system deep on the BEC side of the BEC-BCS crossover. In this regime:
- Delta ~ lambda_min (algebraic, not exponential)
- Gap RATIOS between sectors are preserved: Delta_1/Delta_2 ~ lambda_min,1/lambda_min,2
- The exponential amplification that destroys phi is absent

**Paasch's quantification** (Round 2): Rescue is PARTIAL and sector-dependent. (0,0) has M_max ~ 6-10 (strongly BEC), but (3,0) has M_max ~ 1.2-2.4 at mu=lambda_min (marginal). In the mixed regime, the dressed ratio phi_BCS is estimated 3-8% below phi_paasch.

**Consensus**: BEC-side rescues phi_paasch from the exponential destruction proof, but the partial rescue still leaves a ~3-8% deviation that compounds with the 5% tau-mismatch deviation.

### II.4 R_BCS Is UV-Safe (Truncation-Independent)

**Landau's proof** (Round 1, Point 4): R_BCS = (m_3^2 - m_2^2)/(m_2^2 - m_1^2) is a ratio of eigenvalue differences within a SINGLE Peter-Weyl sector. By the D_K block-diagonality theorem (Session 22b, 8.4e-15), these eigenvalues are determined entirely by one sector's representation content. Adding higher (p,q) sectors cannot change eigenvalues in lower sectors. R_BCS is EXACTLY truncation-independent.

**Implication**: The L-8 sector convergence failure (482%) does NOT affect R_BCS, phi_paasch, or any per-sector eigenvalue ratio. It affects only global sums (total condensation energy, cosmological constant estimate). UV-safe quantities should be prioritized as diagnostics.

### II.5 d_eff Requires Inter-Sector Coupling (Multiplicity Is Not Dimensionality)

**Dispute**: Paasch argued (Round 2) that intra-sector multiplicity dim(3,0)^2 = 100 provides d_eff > 1, analogous to a 100-leg ladder.

**Landau's refutation** (Round 3): The 100 copies are SU(3) symmetry images with identical gap equations. The Kosmann kernel K_a acts as I_V tensor K_a -- identity on the multiplicity space (confirmed from Session 22 data). The 100 copies decouple into 100 identical, independent 1D gap equations. Multiplicity provides thermodynamic extensivity (condensation energy scales as dim^2) but NOT transverse spatial dimension for order parameter fluctuations.

**Paasch's concession** (Round 3): "Landau wins this one." The identity operator on the multiplicity space means no inter-copy coupling. 100 parallel uncoupled 1D wires remain effectively 1D.

**Consequence**: Each sector's BCS condensate is a 1D Luther-Emery liquid with algebraic pairing correlations but no true long-range order. True d_eff >= 2 requires the 1-loop inter-sector coupling computation. This computation is NECESSARY and should be a Session 29 priority.

**Softening** (Landau): Large multiplicity (100-225) quantitatively suppresses quantum fluctuations (coherence length xi ~ xi_0 * sqrt(dim^2)). Quasi-long-range order with xi >> L_K may be operationally sufficient for modulus freezing even without true long-range order.

---

## III. Critical New Result: R_BCS = R_bare

### III.1 The Cancellation

**Neutrino's discovery** (Round 2, Point 3): All three neutrino mass candidates reside in the (0,0) singlet sector (confirmed by block-diagonality theorem + bowtie eigenvalue structure). Within a single sector, the BCS gap Delta is uniform (one value for all modes in s-wave mean-field). Under uniform BCS dressing:

```
R_BCS = ((lambda_3^2 + Delta^2) - (lambda_2^2 + Delta^2)) / ((lambda_2^2 + Delta^2) - (lambda_1^2 + Delta^2))
      = (lambda_3^2 - lambda_2^2) / (lambda_2^2 - lambda_1^2)
      = R_bare
```

The Delta^2 terms cancel identically. R_BCS = R_bare = 5.68 (from Session 24a K_a cross-check). The BCS condensate does NOT change the neutrino mass-squared ratio.

### III.2 The Mode-Dependent Gap Escape Route

**Landau's identification** (Round 3): The tridiagonal Kosmann kernel V(n,m) within the (0,0) sector is NOT constant -- it has nearest-neighbor structure. The self-consistent BCS gap equation with mode-resolved V(n,m) produces a mode-dependent gap Delta_n that varies along the eigenvalue ladder. This makes R_BCS != R_bare generically.

**Neutrino's quantitative assessment** (Round 3): The escape route exists but likely pushes R in the WRONG direction.
- V_{12} ~ 0.10 > V_{23} ~ 0.02 (measured hierarchy)
- Delta_1 couples more strongly to Delta_2 than Delta_3 does
- Therefore Delta_1 > Delta_3, which INCREASES the denominator of R relative to the numerator
- R_BCS < R_bare (further from the target of 33)

**Landau's counter** (Round 3): The direction is unknown without the full mode-resolved BdG computation. The qualitative sign argument is suggestive but not definitive.

### III.3 Panel Assessment

| Position | R_BCS status | Next step |
|:---------|:------------|:----------|
| Neutrino | Effectively CLOSED. Mode-dependent correction likely worsens R. | Tridiagonal PMNS extraction replaces R_BCS as top neutrino diagnostic. |
| Landau | OPEN. Mode-resolved BdG is the correct computation. Direction unknown without calculation. | Mode-resolved BdG within (0,0) at tau=0.35 (and 0.15). |
| Coordinator | Formally OPEN but UNFAVORABLE. Document as "escape route exists, expected sign unfavorable, computation needed." | Include in Session 29 priority list. |

---

## IV. Key Downgrade: phi_paasch Reclassified

### IV.1 Paasch's Final Position (Round 3)

phi_paasch = m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 (Session 12, 0.0005% match) is reclassified from **physical prediction** to **mathematical property of the D_K spectrum**.

**Quantitative evidence**:

| tau | r = E_{(3,0)}/E_{(0,0)} | Deviation from phi_paasch |
|:----|:------------------------|:-------------------------|
| 0.10 | 1.537088 | +0.36% |
| 0.15 | ~1.531580 | +0.0005% |
| 0.20 | 1.519977 | -0.76% |
| 0.30 | 1.481520 | -3.27% |
| 0.35 | ~1.455 | ~-5.0% |

The BCS interior minimum at tau=0.35 places the physical mass ratio 5% away from phi_paasch -- well outside the pre-registered 1% tolerance.

### IV.2 Residual Evidential Weight

- The 5 ppm match at tau=0.15 is pre-registered (Session 12) and survives trial-factor correction
- Reclassified as evidence for the ALGEBRAIC STRUCTURE of D_K on SU(3), not for the framework's mass predictions
- Belongs in the pure-math paper (Einstein's E-6 proposal, "Spectral Anatomy of D_K on Jensen-Deformed SU(3)")
- Bayes factor downgraded: BF = 5 (Session 22a) -> BF = 2 (MARGINAL)

### IV.3 Remaining Rescue Scenarios

1. **Backreaction shifts tau_0**: If the coupled modulus-BCS equation places the frozen tau closer to 0.15 than the uncoupled minimum at 0.35. Requires Landau's backreaction computation.
2. **BEC-side preservation**: Landau confirmed algebraic (not exponential) gap ratios on BEC side. But partial rescue only (3-8% additional deviation from mixed BEC/BCS regime).
3. **D_can spectrum**: Torsion compression is non-uniform across sectors. phi_paasch in D_can has not been computed.

None of these are expected to fully restore phi_paasch, but scenario 1 is the most consequential.

---

## V. The Tau Mismatch: A Tension Turned Discriminator

All three specialists independently flagged the tau mismatch: phi_paasch lives at tau=0.15, the BCS minimum at tau=0.35. Round 2 deliberation transformed this from a "tension" to a "discriminator":

**Neutrino's reframing** (Round 2, Point 2): Computing R_BCS (and PMNS angles) at BOTH tau=0.15 and tau=0.35 turns the mismatch into a diagnostic. If observables pass at one tau but not the other, the data tells us where the modulus froze. The framework cannot have it both ways -- it must commit to a physical tau_0.

**Landau's nucleation analysis** (Round 3, ITEM 2): In a first-order transition, nucleation occurs at tau_coexistence (where BCS and normal-state free energies are equal), NOT at the point of maximum gap (tau=0.15) or the thermodynamic minimum (tau=0.35). Estimated tau_nucleation in [0.20, 0.35]. Requires the backreaction computation to resolve.

**Paasch's concession** (Round 3, ITEM 1): "The evidence favors tau=0.35. The tau mismatch is a genuine problem I cannot resolve with current data."

**Synthesis**: The physical tau_0 is determined by the backreaction dynamics, which is the #2 Session 29 priority. All three specialists' diagnostics should be evaluated at the backreaction-determined tau_0, with tau=0.15 and tau=0.35 as bracket values.

---

## VI. Landau's d_eff Fork Resolution

### VI.1 The Apparent Contradiction

d_eff >= 2 (true long-range order) seems to require coherent cross-sector condensate with universal gap (compresses R toward 1, bad for neutrinos). d_eff < 2 (independent sectors) preserves sector-dependent gaps (good for R) but destroys the condensate order (bad for stability).

### VI.2 Landau's Multi-Band Resolution (Round 2)

The order parameter has TWO components:
- **Phase**: The relative phase between sector gaps. Inter-sector Josephson-type coupling locks phases. d_eff for phase coherence can be large (many coupled sectors). This provides true long-range order and frozen modulus.
- **Amplitude**: The magnitude |Delta_i| per sector. Determined by intra-sector pairing. d_eff for amplitude fluctuations remains effectively 1 per sector. Sector-dependent gaps are preserved.

**Condensed matter precedent**: MgB2, iron pnictides, multi-band cold atom systems. Phase locking without amplitude equalization is established physics.

**Requirement**: The 1-loop inter-sector Josephson coupling J_ij must be computed. If J_ij > 0, phases lock and both branches of the fork are satisfied simultaneously.

### VI.3 Implication for Neutrinos

Even with the d_eff fork resolved, the neutrino R issue (Section III) persists because R is an INTRA-sector quantity. The multi-band resolution affects inter-sector ratios (phi_paasch) but not intra-sector mass-squared ratios (R). The neutrino program is downstream of d_eff but not saved by it.

---

## VII. Updated Neutrino Prediction Pipeline

| Step | Description | Status (Post-28, Post-Synthesis) |
|:-----|:------------|:--------------------------------|
| 1 | Fix tau_0 | CONDITIONALLY UNBLOCKED (BCS at tau=0.35, pending KC-3 + backreaction) |
| 2 | Extract lightest eigenvalues at tau_0 | Ready |
| 3 | Convert to physical mass units | Blocked (L_K from condensation scale uncomputed) |
| 4 | Compute PMNS from within-sector overlaps | Ready (tridiagonal selection rules constrain structure) |
| 5 | Compare R against [17, 66] | EFFECTIVELY CLOSED (R_BCS = R_bare = 5.68, mode-dependent correction unfavorable) |
| 5' | Compare PMNS angles against data | OPEN (tridiagonal extraction not yet computed) |

**Pipeline status**: Step 5 (mass ratio) is effectively closed. Step 5' (mixing angles) is the last remaining neutrino-specific test. Steps 1 and 3 remain coupled to the stabilization mechanism.

---

## VIII. Session 29 Priority Ranking (Consensus)

| Priority | Computation | Rationale | Cost | UV-Safe? |
|:---------|:-----------|:----------|:-----|:---------|
| 1 | KC-3 at tau >= 0.50 | Constraint Chain completion, consensus top priority | Medium | N/A |
| 2 | Backreaction self-consistency | Determines WHERE tau freezes, resolves tau mismatch for all domains | Medium | N/A |
| 3 | Tridiagonal PMNS extraction | Last remaining neutrino gate: sin^2(theta_13) in [0.015,0.030], theta_12 in [28,38] deg | Low | Yes |
| 4 | phi_paasch in D_can spectrum | Non-uniform torsion compression may shift ratio; zero-cost from existing .npz | Low | Yes |
| 5 | Mode-resolved BdG within (0,0) | Settles R_BCS != R_bare question and sign of correction | Low | Yes |
| 6 | Leggett crossover parameter | BEC vs BCS determination per sector; interpretive value | Low | Yes |
| 7 | 1-loop inter-sector coupling for d_eff | Determines true vs quasi-long-range order; all domains affected | High | N/A |

**Notes on ranking**:
- #1 and #2 are consensus across all specialists
- #3 elevated by Neutrino after R_BCS cancellation discovery (replaces R_BCS as top neutrino diagnostic)
- #4 proposed by Paasch, supported by all
- #5 resolves the Neutrino-Landau partial disagreement on mode-dependent gap direction
- #6 proposed by Neutrino, supported by Landau (informational, helps interpret all BCS results)
- #7 proposed by Landau, supported by Paasch (after conceding multiplicity argument), high cost but affects all domains

---

## IX. Framework Probability Assessment

### IX.1 Individual Assessments

| Specialist | Panel estimate | Sagan estimate | Key drivers |
|:-----------|:--------------|:---------------|:-----------|
| Neutrino | 7-9% | 4-6% | Concurs with Baptista range; neutrino-specific probability near zero until PMNS computed; R_BCS cancellation is negative |
| Landau | 8-10% | 5-7% | Constraint Chain physically coherent; BEC-side strong coupling validates van Hove mechanism; d_eff unresolved but quasi-order may suffice |
| Paasch | 7-9% | 4-6% | phi_paasch downgraded to mathematical property (BF 5->2); van Hove zero-critical-coupling matches mass quantization requirement |

### IX.2 Synthesis Assessment

**Panel**: 7-10%, median **8%** (range reflects d_eff uncertainty and mode-dependent gap open question)
**Sagan**: 4-7%, median **5%**

**Movements relative to pre-synthesis baseline (5% panel, 3% Sagan)**:
- Upward pressure (+2-3 pp): Constraint Chain physical coherence confirmed by condensed matter analysis; BEC-side validates strong-coupling regime; first-order character structurally necessary and present; van Hove zero-critical-coupling matches Paasch requirement
- Downward pressure (-1 pp): R_BCS = R_bare cancellation (neutrino mass ratio not rescued); phi_paasch downgraded (tau mismatch unresolved); d_eff < 2 risk (no true long-range order)
- Net: +1-3 pp panel, +1-2 pp Sagan

---

## X. Open Disagreements (Documented, Not Resolved)

### X.1 Mode-Dependent Gap Direction (Neutrino vs Landau)

**Neutrino**: V_{12} > V_{23} implies Delta_1 > Delta_3, which DECREASES R_BCS below R_bare (wrong direction). The escape route is open but unfavorable.

**Landau**: The qualitative sign argument is suggestive but not definitive. The full mode-resolved BdG computation is needed. Direction is unknown.

**Resolution pathway**: Priority #5 (mode-resolved BdG within (0,0)). Zero-parameter computation from existing data.

### X.2 Tau Nucleation Location

**Landau**: tau_nucleation in [0.20, 0.35], determined by coexistence condition (Maxwell construction), not by maximum gap.

**Paasch**: Evidence against tau=0.15 (self-refuted), favors tau=0.35 but cannot prove it without backreaction computation.

**Resolution pathway**: Priority #2 (backreaction self-consistency). Coupled modulus-BCS dynamics equation.

---

## XI. Structural Results (Permanent, Unchanged by Session 28)

These survive all Session 28 results and the Team C deliberation:

1. **CPT invariance**: [J, D_K(tau)] = 0 identically
2. **Three generations**: Z_3 triality (LEP N_nu = 2.984 consistency)
3. **Normal mass ordering**: Bowtie eigenvalue structure at tau_0 > 0.20 (testable by JUNO/DUNE)
4. **PMNS hierarchy**: theta_12 >> theta_13 from tridiagonal selection rules V(L1,L3) = 0
5. **KO-dimension = 6**: Parameter-free, SM signature
6. **D_K block-diagonality**: Exact at 8.4e-15, any left-invariant metric on compact Lie group
7. **phi_paasch at tau=0.15**: 0.0005% match (mathematical property of D_K spectrum)
8. **Van Hove zero-critical-coupling**: ANY V > 0 produces Delta > 0 with van Hove DOS

---

*Synthesis completed by Coordinator, 2026-02-27. Three-round deliberation with Neutrino (neutrino-detection-specialist), Landau (landau-condensed-matter-theorist), Paasch (paasch-mass-quantization-analyst). All assessments traceable to the 3 input collab files and 9 rounds of inter-specialist messaging.*
