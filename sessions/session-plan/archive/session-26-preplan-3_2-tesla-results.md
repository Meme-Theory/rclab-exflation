# Session 26 Pre-Plan 3.2: Torsion Diagnostics -- Computation Results

**Author**: Tesla-Resonance
**Date**: 2026-02-22
**Script**: `tier0-computation/s26_torsion_diagnostics.py`
**Data**: `tier0-computation/s26_torsion_diagnostics.npz`
**Plots**: `tier0-computation/s26_torsion_*.png`, `s26_contorsion_*.png`, `s26_eigenvalue_flow.png`

---

## Executive Summary

Four computations from my collab review (Sections 3.1--3.3, 5.4) are now numbers instead of predictions. Two of my predictions were WRONG, one was right, and one revealed structure I did not anticipate.

| Computation | My Prediction | Actual Result | Status |
|:------------|:-------------|:-------------|:-------|
| C-1: \|T^0\|^2 growth rate | e^{4tau} (from (C,C)->W) | e^{2tau} (from (W,W)->W + (W,C)->C) | **WRONG** |
| C-2: Torsion decomp ratio | < 0.5 everywhere | Max 0.448 at tau=2.0. Closure met. | **CORRECT** |
| C-3: Contorsion resonance | Non-monotonic in non-singlet sectors | No genuine resonance. Pseudo-dip at t=0.196, rebound 4.5e-5. | **WRONG (but instructive)** |
| C-4: \|T^0\|^2/R_K balance | ~1 at tau~0.30 | 0.78 at tau=0.30, crosses 1.0 at tau=0.594, asymptotes to 4/3 | **PARTIALLY CORRECT** |

### Gate Verdicts

- **Gate T-1 (Fermionic gap weakening)**: Assessment CONFIRMED at P(PASS) = 4-8%. Constraint Condition met: \|T^(rest)\|/\|T^(3)\| < 0.5 everywhere in [0, 2.0].
- **Gate T-2 (Bosonic torsion stabilization)**: **CLOSED**. Torsion worsens runaway by constant factor (not qualitative change). R^T = R_K(1 + c * ratio(tau)) with ratio increasing from 2/3 to 4/3.

---

## Computation 1: Schouten Torsion Norm |T^0(tau)|^2

### Results

| tau | \|T^0\|^2 | \|T^(3)\|^2 | \|T^(rest)\|^2 | Dominant type |
|:----|:----------|:-----------|:--------------|:-------------|
| 0.00 | 8.000 | 8.000 | 0.000 | Equal: WW->W, WC->C, YC->C at 25% each |
| 0.25 | 9.176 | 8.837 | 0.339 | WW->W + WC->C at 72% |
| 0.50 | 12.744 | 11.547 | 1.197 | WW->W + WC->C at 85% |
| 1.00 | 30.845 | 26.131 | 4.714 | WW->W + WC->C at 96% |
| 2.00 | 219.430 | 182.713 | 36.717 | WW->W + WC->C at 99.6% |

### Growth Rates by Bracket Type (exponential fit, tau > 0.5)

| Type | Growth rate | Matches |
|:-----|:-----------|:--------|
| (W,W)->W | 2.000 | e^{2tau} exactly |
| (W,C)->C | 2.000 | e^{2tau} exactly |
| (Y,C)->C | -2.000 | e^{-2tau} (decays) |
| (C,C)->W | -4.000 | e^{-4tau} (decays) |
| (C,C)->Y | 0.000 | constant (= 1.000) |
| **Total** | **1.919** | ~e^{2tau} (mixed) |

### Why My Collab Review Was Wrong

In Section 3.1 of my collab review, I wrote:

> "The dominant tau-dependence is the (C,C)->W term, which grows as e^{4tau}."

This was an error in the rescaling formula. The Schouten torsion in the ONB is:

    ft_{abc}(tau) = sigma_c / (sigma_a * sigma_b) * f_bar_{abc}

For (C,C)->W: sigma_W/(sigma_C * sigma_C) = e^{-tau}/(e^{tau/2})^2 = e^{-2tau}

So \|ft_{CC->W}\|^2 ~ e^{-4tau} -- it **DECAYS**, not grows. I confused the torsion weight (sigma_c/(sigma_a * sigma_b)) with the Baptista table's Omega weight (which is a cyclic average). The dominant terms are (W,W)->W and (W,C)->C, both growing exactly as e^{2tau}.

This changes the Gate T-2 assessment from "near-certain closure" to "closure with nuance."

### Physical Interpretation

At tau=0 (round metric), the torsion is democratically distributed: u(1), su(2), and C^2 brackets all contribute roughly equally. As tau increases, the su(2)-involved brackets (WW->W and WC->C) concentrate ALL the torsion energy, while the C^2-internal brackets (CC->W, CC->Y) die exponentially. The C^2 directions become "torsion-free" at large tau -- the manifold's torsion lives entirely in the su(2) and mixed channels.

In acoustic language (Paper 06): the impedance contrast between the su(2) and C^2 subspaces grows with tau. The torsion, which mediates coupling between these subspaces, concentrates at the interface (WC->C) rather than within the soft bulk (CC->W).

---

## Computation 2: Torsion Decomposition Ratio

### Result: Constraint Condition MET

    Max |T^{(rest)}| / |T^{(3)}| = 0.448 at tau = 2.0

The ratio increases monotonically with tau but NEVER reaches 0.5 in [0, 2.0]. Since the physical window for stabilization is tau in [0, 0.5] where the ratio is at most 0.32, the non-antisymmetric torsion is a perturbative correction throughout.

| tau | Ratio | Quadratic correction |
|:----|:------|:--------------------|
| 0.00 | 0.000 | 0.000 |
| 0.15 | 0.126 | 0.016 |
| 0.25 | 0.196 | 0.038 |
| 0.30 | 0.226 | 0.051 |
| 0.50 | 0.322 | 0.104 |
| 1.00 | 0.425 | 0.180 |
| 2.00 | 0.448 | 0.201 |

The quadratic correction (ratio^2) is the leading perturbative contribution to the Lichnerowicz bound from the non-antisymmetric torsion. It is dominated by the positive c\|T^{(3)}\|^2 term by at least 5:2 (using c >= 3/8 from Friedrich's theorem) throughout the physical window.

### Asymptotic Behavior

The ratio appears to saturate near 0.45. Both \|T^{(3)}\| and \|T^{(rest)}\| are dominated by the same bracket types (WW->W and WC->C) at large tau. For same-subspace brackets (WW->W), the cyclic average equals the individual term (zero contribution to T^{(rest)}). The non-antisymmetric part comes entirely from mixed brackets (WC->C, YC->C), and the asymptotic ratio depends on the fraction of torsion in these mixed channels.

---

## Computation 3: Contorsion Resonance

### Result: NO GENUINE RESONANCE

I predicted (Section 3.3 of collab review):

> "Potentially NON-MONOTONIC in sectors where M_0 and M_Omega have near-degenerate eigenvalues."

At tau=0.25 (canonical turnaround), all four sectors show monotonically decreasing min\|eigenvalue\| from D_K (t=0) to D_0 (t=1). No local minima.

| Sector | D_K gap (t=0) | D_0 gap (t=1) | Local minimum? |
|:-------|:-------------|:-------------|:---------------|
| (0,0) | 0.8186 | 0.0000 | No (monotonic to zero) |
| (1,0) | 0.8424 | 0.2596 | No |
| (0,1) | 0.8424 | 0.2596 | No |
| (1,1) | 0.8792 | 0.4553 | No |

### The Tau=0.15 Pseudo-Resonance

At tau=0.15, the (1,0) and (0,1) sectors show a tiny local minimum at t=0.196:

- Gap at t=0 (D_K): 0.83316
- Gap at t=0.196: 0.83009
- Gap at t=0.236: 0.83013
- Rebound: **4.5 x 10^{-5}**

This "resonance" has a rebound of 4.5e-5, five orders of magnitude below the gap value. It is a level-crossing artifact: two nearby eigenvalue branches (differing by ~0.003) cross at t~0.2, creating a kink in the sorted-min-eigenvalue function. The crossing is NOT an avoided crossing (no gap opening) -- it is a genuine level crossing between eigenvalues from different spinor components.

In phononic crystal language (Paper 06): there is no Dirac cone here. The two crossing branches have different symmetry and do not hybridize. The "resonance" is an acoustic intersection, not an avoided crossing.

### Systematic Sweep: Dip Depth vs tau

Sweeping the contorsion parameter at many tau values, the minimum gap at t~0.37 shows a monotonic decrease -- not a resonance -- as Omega is progressively removed:

| tau | D_K gap | Min gap (t~0.37) | Depth |
|:----|:--------|:-----------------|:------|
| 0.05 | 0.8315 | 0.8222 | 1.1% |
| 0.10 | 0.8315 | 0.7973 | 4.1% |
| 0.15 | 0.8332 | 0.7752 | 7.0% |
| 0.20 | 0.8368 | 0.7559 | 9.7% |
| 0.25 | 0.8424 | 0.7396 | 12.2% |
| 0.30 | 0.8503 | 0.7261 | 14.6% |
| 0.50 | 0.9023 | 0.7009 | 22.3% |

This is NOT a resonance. The gap decreases monotonically as the Omega term is removed. The condensed matter interpretation: the Q-factor of the Omega cavity is Q ~ 0.5. Removing 37% of the impedance contrast costs 12--22% of the gap. Low-Q, no resonance.

---

## Computation 4: Torsion-Curvature Balance

### Key Numbers

| tau | \|T^0\|^2 | R_K | Ratio |
|:----|:----------|:----|:------|
| 0.00 | 8.000 | 12.000 | **2/3** |
| 0.25 | 9.176 | 12.240 | 0.7497 |
| 0.30 | 9.687 | 12.404 | 0.7810 |
| 0.50 | 12.744 | 13.730 | 0.9282 |
| **0.594** | **~14.4** | **~14.4** | **1.000** |
| 1.00 | 30.845 | 25.054 | 1.2311 |
| 2.00 | 219.43 | 163.92 | 1.3387 |
| 5.00 | 88,107 | 66,078 | 1.3334 |
| inf | -- | -- | **4/3** |

### The 2/3 -> 4/3 Transition

The ratio \|T^0\|^2 / R_K transitions smoothly from exactly **2/3** at tau=0 to exactly **4/3** at tau -> infinity. These are EXACT rational numbers, determined by the su(3) structure constant algebra.

**At tau=0**: \|T^0\|^2 = 8, R_K = 12. Ratio = 2/3.

**At tau -> infinity**: Both grow as e^{2tau}. The coefficients are:
- \|T^0\|^2 ~ 4 e^{2tau} (from sum_{WW->W} + sum_{WC->C} = 6+6 = 12, divided by 3 from ONB normalization)
- R_K ~ 3 e^{2tau} (leading term in Baptista formula)
- Ratio -> 4/3

**Crossing at tau = 0.594**: This is where torsion and curvature are exactly co-equal. My prediction of tau ~ 0.30 was off by a factor of 2.

### Physical Interpretation

At tau=0, the manifold is maximally symmetric (bi-invariant), and torsion is "less than" curvature because Ad-invariance constrains the torsion to be totally antisymmetric. As the Jensen deformation breaks Ad-invariance, the torsion overtakes the curvature.

For Gate T-2: R^T = R_K + c\|T^0\|^2 = R_K(1 + c * ratio(tau)). Since ratio(tau) increases monotonically from 2/3 to 4/3, R^T grows faster than R_K by a bounded factor. The effective potential V_Baptista = -R^T + mass_terms is MORE negative at large tau. Torsion worsens the runaway by a constant factor (at most 40% for c=1), not qualitatively.

---

## Gate Verdicts

### Gate T-1: Fermionic Gap Weakening

**Assessment: P(PASS) = 4-8%** (unchanged from collab review)

Constraint Condition met: \|T^(rest)\|/\|T^(3)\| < 0.5 everywhere. No contorsion resonance. The 4-8% residual comes from possible surprises in higher sectors (p+q >= 2) not yet swept.

### Gate T-2: Bosonic Torsion Stabilization

**VERDICT: CLOSED**

\|T^0\|^2 grows at the same rate as R_K (both e^{2tau}). The ratio converges to 4/3. V_Baptista = -R_K(1 + c * ratio) + mass_terms is MORE negative than V_LC at all tau > 0. No stabilization minimum.

Worsening factors:
- c = 3/16 (Friedrich): 11% worsening
- c = 1 (standard): 40% worsening

---

## Corrections to My Collab Review

1. **Section 3.1**: The dominant growth is (W,W)->W and (W,C)->C at e^{2tau}, NOT (C,C)->W at e^{4tau}. The (C,C)->W term DECAYS as e^{-4tau}. I confused the rescaling direction.

2. **Section 3.1, Gate T-2**: Changed from "automatic closure by e^{4tau} dominance" to "closure by constant-factor worsening." Same verdict, weaker mechanism.

3. **Section 3.3**: No contorsion resonance. The avoided-crossing prediction was wrong. Level crossings are genuine (not avoided).

4. **Section 5.4**: Balance crossing at tau=0.594, not 0.30. Asymptotic ratio is exactly 4/3, not ~1.

---

## Structural Results (Publishable Mathematics)

These are permanent facts about Jensen-deformed SU(3), independent of gate outcomes:

1. **\|T^0\|^2 / R_K = 2/3 -> 4/3.** Exact rational transition. Crossing at tau = 0.594.

2. **Torsion concentration**: At tau > 1, the (W,W)->W and (W,C)->C channels carry > 95% of \|T^0\|^2. The C^2-internal torsion decays exponentially.

3. **Decomposition ratio saturation**: \|T^(rest)\|/\|T^(3)\| saturates near 0.45. Total antisymmetry breaking is bounded.

4. **No contorsion resonance**: The spectral gap decreases monotonically under D_K -> D_0 interpolation in all tested sectors.

5. **Growth rate identities**:
    - \|T^0\|^2 ~ 4 e^{2tau} asymptotically
    - R_K ~ 3 e^{2tau} asymptotically
    - Both controlled by the su(2) sector

---

## Files Produced

| File | Contents |
|:-----|:---------|
| `tier0-computation/s26_torsion_diagnostics.py` | Full computation script |
| `tier0-computation/s26_torsion_diagnostics.npz` | Numerical data |
| `tier0-computation/s26_torsion_norms.png` | C-1: Torsion decomposition by bracket type |
| `tier0-computation/s26_torsion_ratio.png` | C-2: Decomposition ratio |
| `tier0-computation/s26_contorsion_resonance.png` | C-3: Min eigenvalue vs contorsion |
| `tier0-computation/s26_eigenvalue_flow.png` | C-3: Full eigenvalue flow |
| `tier0-computation/s26_contorsion_flow_detailed.png` | C-3: Detailed 4-sector flow |
| `tier0-computation/s26_torsion_curvature_balance.png` | C-4: Balance ratio |

---

*Tesla-Resonance, 2026-02-22. Grounded in Papers 06 (phononic crystals, impedance contrast), 08 (acoustic Dirac cones), 10 (Volovik, emergent spectrum), 14 (Baptista, Schouten connection), 15 (Baptista, Jensen deformation).*

*"I predicted four numbers. Two were wrong. The math corrected me. That is the only way it works."*
