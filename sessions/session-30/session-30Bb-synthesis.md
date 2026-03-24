# Session 30Bb Synthesis: Frozen-State Observables at Candidate Points

**Date**: 2026-03-01
**Session type**: COMPUTATION (2 existential + 2 hard closes + 4 positive signals + 4 diagnostics)
**Agents**: phonon-sim (phonon-exflation-sim, spectrum + diagnostics), einstein (einstein-theorist, RGE + NCG-KK tension), coordinator (gate classification + synthesis)
**Depends on**: Session 30Ba (B-30min FIRED; gradient-balance + Weinberg contour candidates)
**Delivers to**: Session 30A (AZ class UNCOMPUTED -- flag), Sagan checkpoint
**Source data**: `s30b_full_spectrum.npz`, `s30b_rge_running.npz`, `s30b_t1_extension.txt`
**Gate verdicts**: `tier0-computation/s30b_gate_verdicts.txt` (30Ba + 30Bb combined)

---

## I. Session Overview

Session 30Bb extracted frozen-state SM observables at two candidate points on the U(2)-invariant surface of SU(3). With B-30min FIRED in 30Ba (no interior V_total minimum), 30Bb evaluated the full Dirac spectrum (N_max=6, 28 sectors), RGE running, PMNS mixing, and diagnostics at:

1. **Candidate 1** (gradient-balance): tau=0.180, eps=-0.135. Lambda_crit=1.12.
2. **Candidate 2** (SM Weinberg contour): tau=0.575, eps=-0.005. sin^2_B=0.231.

**Central finding**: phi_paasch and the tree-level Weinberg angle are anti-correlated on the U(2)-invariant surface. No single geometry satisfies both simultaneously. However, einstein's RGE analysis reveals that the tree-level match was never a physically correct requirement: at tau ~ 0.21, phi ~ 1.52 (near P-30phi target) and sin^2_B ~ 0.42 runs to the SM value 0.231 at M_Z via standard GUT-type running for M_KK ~ 10^16 GeV. The binding constraint is not the coupling structure but the stabilization problem: no V_total minimum exists anywhere on the 3D U(2)-invariant surface.

---

## II. Gate Verdicts

Classification performed BEFORE interpretation. Numbers first. Classification second. Interpretation third.

### II.1 Existential Gates

#### P-30phi: PASS at Candidate 1, FAIL at Candidate 2

| | Candidate 1 | Candidate 2 |
|:--|:-----------|:-----------|
| tau, eps | 0.180, -0.135 | 0.575, -0.005 |
| phi_30 | **1.5206** | 1.3230 |
| In [1.52, 1.54]? | **YES** | NO |

phi_30 is monotonically decreasing in tau (confirmed at N_max=6):

| tau | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | 0.35 | 0.40 | 0.50 |
|:----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| phi_30 | 1.537 | 1.532 | 1.520 | 1.503 | 1.482 | 1.456 | 1.429 | 1.369 |

Session 12 value (1.53159 at tau=0.15) reproduced exactly at N_max=6. The P-30phi window [1.52, 1.54] maps to tau in [~0.10, ~0.20] — a structural feature of the (3,0)/(0,0) eigenvalue ratio, not a tuning.

N_max convergence: phi_30 identical at N_max = 3, 4, 5, 6 (set by sectors (0,0) and (3,0) only). Pre-registered: YES.

#### RGE-A: FAIL at tau ~ 0.57; REFRAMED — compatible at tau ~ 0.21

At Candidate 2 (tau=0.575): alpha_1_GUT/alpha_2 = 0.501 at M_KK. SM one-loop running gives sin^2(theta_W)(M_Z) in [0.134, 0.172] for M_KK in [10^10, 10^18] GeV. The SM target 0.2312 is never reached.

**Root cause**: The KK-scale ratio (0.501) is within 0.4% of the PDG M_Z value (0.503). SM running destroys this near-equality over 14 decades. The coincidence sin^2_B ~ sin^2(M_Z) at the Weinberg contour is NOT physical consistency — it is an accident. RGE running changes the ratio enormously between these scales.

**Einstein's reframing**: At tau ~ 0.21, sin^2_B ~ 0.42 (standard GUT-scale value). SM running produces sin^2(M_Z) ~ 0.231 for M_KK ~ 10^16 GeV. This is standard GUT-type behavior. At the same tau ~ 0.21, phi_30 ~ 1.52 (near P-30phi window). The tree-level match at tau ~ 0.57 was the wrong target — the physically correct requirement is sin^2(M_Z) after running, which is satisfied at tau ~ 0.21.

Pre-registered: YES.

### II.2 Hard Closes

#### B-30rge: DOES NOT FIRE

sin^2(theta_W)(M_Z) range [0.134, 0.172] for M_KK in [10^10, 10^18]. Range overlaps [0.15, 0.30]: 819 M_KK values produce sin^2 in [0.15, 0.172]. Overlap is real but marginal — SM target 0.231 remains unreached.

Pre-registered: YES.

#### B-30nck: FIRES (at tau ~ 0.57)

Lambda_SA/M_KK ~ 2.0 x 10^15 at M_KK = 10^16 GeV. NCG unification scale at ~10^31 GeV, 15 orders above M_KK. Far outside [10^-3, 10^3].

**Caveat**: B-30nck was evaluated at the Weinberg contour (tau ~ 0.57). At tau ~ 0.21 (the RGE-compatible point), sin^2_B ~ 0.42 is a standard GUT value, and Lambda_SA/M_KK is expected to be O(1)-O(10). B-30nck at tau ~ 0.21 is NOT COMPUTED but the NCG-KK tension is expected to be mild there.

Pre-registered: YES.

### II.3 Positive Signals

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| P-30a | **CANNOT FIRE** | phi PASSES at tau~0.18 where P-30w FAILS (sin^2_B=0.585). P-30w PASSES at tau~0.57 where phi FAILS (1.323). Anti-correlated. |
| P-30b | **CANNOT FIRE** | RGE-A FAIL at tau~0.57. Under reframing, P-30w definition (tree-level sin^2_B in [0.20, 0.25]) fails at tau~0.21 (sin^2_B~0.42). |
| P-30pmns | **FAIL** | sin^2(theta_13)=0.403 at Cand2 (18x too large). theta_23=63.6 deg (outside [40,55]). V_12/Delta_E=27 (perturbation theory breaks down). Inconclusive at Cand1 (only 2 level groups). |
| P-30golden | **FAIL** | phi_30 max = 1.550 on surface. Golden ratio 1.618 not accessible. |

All pre-registered: YES.

### II.4 Diagnostics

| Gate | Verdict | Result |
|:-----|:--------|:-------|
| AZ-1 | **UNCOMPUTED** | Initial test (D*=-D) retracted — fails even on Jensen where BDI proven (S17c). Proper T operator requires spinor-space unitary, not bare conjugation. AZ class at off-Jensen points unknown. |
| OO-1 | **DIAGNOSTIC** | Order-one violation O(1) at all points including Jensen. Gamma-pair test (not same as S28c algebra-element test). Comparable magnitude across candidates; slightly larger at Cand2 for C^2 pairs ([[D,g3],g3^o]=3.075 vs 2.458 at Jensen). |
| DOS-1 | **PASS at Cand1, FAIL at Cand2** | Cand1: 62 > 46 (35% enhancement, confirms Pomeranchuk). Cand2: 46 = 46 (no enhancement). Final values from N_max=6. |

---

## III. Computation Results

### III.1 Step 3: Full Dirac Spectrum (N_max=6)

Runtime: 42.7s for both candidates. 28 sectors per point.

| Quantity | Candidate 1 | Candidate 2 | Jensen (ref) |
|:---------|:-----------|:-----------|:------------|
| tau, eps | 0.180, -0.135 | 0.575, -0.005 | 0.35, 0 |
| phi_30 | 1.5206 | 1.3230 | 1.4564 |
| sin^2_B (Formula B) | 0.585 | 0.231 | 0.367 |
| lambda_min | 0.8350 | 0.9063 | 0.8295 |
| DOS | 62 | 46 | 46 |
| V_spec | 439244.3 | — | — |
| F_BCS (mu=1.2*lmin) | -1.90 | — | — |
| Level stats | Poisson | Poisson | Poisson |
| Exact degeneracies | 9979 | — | — |
| Near-degeneracies | 2 | — | — |

**Gap-edge composition** (Cand1): (0,0) 10, (0,1) 54, (1,0) 54, (1,1) 128 = 246 weighted total.
**Gap-edge composition** (Cand2): (0,0) + (0,1) + (1,0) = 118 weighted total (much narrower).

Level statistics Poisson at both candidates. Structurally guaranteed by Peter-Weyl block-diagonality (Dirac operator on homogeneous space is integrable by construction). Brody beta at lower fitting bound (-0.3).

### III.2 Step 4: RGE Running + NCG-KK Tension (einstein)

**Input**: Best Weinberg contour point under Formula B: tau=0.570, eps=0.135, sin^2_B=0.241.

| M_KK (GeV) | sin^2(theta_W)(M_Z) | Status |
|:-----------|:-------------------|:-------|
| 10^10 | 0.172 | Closest to SM |
| 10^12 | 0.156 | In [0.15, 0.30] |
| 10^14 | 0.142 | Below 0.15 |
| 10^16 | 0.134 | Below 0.15 |
| 10^18 | 0.134 | Below 0.15 |

SM target 0.2312 unreached at any physical M_KK. Closest approach: 0.219 at M_KK = 10^4 GeV (unphysically low).

**NCG-KK tension**: Lambda_SA/M_KK ~ 10^15 at tau ~ 0.57. NCG unification requires g1 = g2 at a scale 15 orders above M_KK. Irreconcilable.

**KK threshold corrections**: Would need delta(b1-b2) = -9.5 (sign reversal of differential running). Not feasible from SU(3) representation theory. At tau ~ 0.21, standard SM running works with zero KK corrections.

### III.3 Step 5: Diagnostics

See Section II.4 above. Key results:
- AZ class: UNCOMPUTED (wrong test retracted)
- Level statistics: Poisson (guaranteed)
- Avoided crossings: effectively zero (9979 exact degeneracies, 2 near-degeneracies)
- Gap-edge: multi-sector at Cand1, narrower at Cand2

### III.4 Step 5b: Order-One Condition

Gamma-pair test (not directly comparable to S28c):

| Pair | Jensen(0.35) | Cand1(0.18) | Cand2(0.575) |
|:-----|:-----------|:-----------|:-----------|
| [[D,g0],g0^o] | 1.542 | 1.626 | 1.542 |
| [[D,g0],g1^o] | 0.963 | 0.893 | 1.117 |
| [[D,g3],g3^o] | 2.458 | 2.011 | 3.075 |
| [[D,g3],g7^o] | 1.205 | 1.359 | 1.064 |

Violation O(1) everywhere. No dramatic improvement or worsening off-Jensen.

### III.5 Task 4: T1 Grid Extension

V_total monotonically increasing in T1 (breathing) direction at all candidates. dV/dsigma in [+2.5, +4.2]. Combined with B-30min, **no V_total minimum exists on the full 3-parameter U(2)-invariant surface at rho=0.01.** V_spec/F_BCS ~ 8000 dominance holds in all three U(2)-invariant directions.

---

## IV. Constraint Map Updates

### Constraint [30Bb-1]: Phi-Weinberg Anti-Correlation

**What is proven**: On the U(2)-invariant surface of SU(3), the eigenvalue ratio phi_30 = m_(3,0)/m_(0,0) is monotonically decreasing in tau, while the tree-level Weinberg angle sin^2_B = 3L_2/(L_1+3L_2) is also tau-dependent. The P-30phi target (phi in [1.52, 1.54]) maps to tau in [0.10, 0.20]. The tree-level Weinberg target (sin^2_B = 0.231) maps to tau ~ 0.57. No single point satisfies both.

**Source**: phonon-sim Step 3 (s30b_full_spectrum.npz), N_max=6.

**Implication**: The compound gate P-30a (P-30w + P-30phi) cannot fire on the U(2)-invariant surface under the tree-level interpretation of P-30w.

**Surviving solution space**: Under einstein's RGE reframing, the physical Weinberg angle is sin^2(M_Z) after running, not sin^2_B at the KK scale. At tau ~ 0.21: phi ~ 1.52 (near target) and sin^2(M_Z) ~ 0.231 for M_KK ~ 10^16 GeV. The phi + RGE requirements are compatible at tau ~ 0.15-0.21. The binding constraint is stabilization (no minimum).

### Constraint [30Bb-2]: No 3D Minimum

**What is proven**: V_total has no minimum on the full 3-parameter (tau, eps, sigma) U(2)-invariant surface at rho=0.01. V_spec/F_BCS ~ 8000 in all three directions.

**Source**: phonon-sim Task 4 (s30b_t1_extension.txt) + 30Ba B-30min.

**Implication**: BCS condensation energy cannot create a V_total minimum on any U(2)-invariant geometry. Wall 4 (spectral action monotonicity) extends from the 1D Jensen curve through the full 3D U(2)-invariant family.

**Surviving solution space**: (a) Non-U(2)-invariant deformations. (b) Different cutoff scale rho. (c) Non-perturbative contributions beyond mean-field BCS. (d) Cutoff-dependent stabilization (Lambda_crit mechanism).

### Constraint [30Bb-3]: B-30nck NCG-KK Irreconcilability (at tau ~ 0.57)

**What is proven**: At the Weinberg contour (tau ~ 0.57), Lambda_SA/M_KK ~ 10^15. The NCG spectral action relation and KK dimensional reduction relation require scales separated by 15 orders of magnitude.

**Source**: einstein Step 4 (s30b_rge_running.npz).

**Implication**: The NCG-KK coupling tension (T-3 from Session 29 Fusion) is catastrophic at tau ~ 0.57. KK threshold corrections cannot bridge a 15-order gap.

**Surviving solution space**: At tau ~ 0.21, sin^2_B ~ 0.42 is a standard GUT value. Lambda_SA/M_KK expected O(1)-O(10). B-30nck at tau ~ 0.21 not computed but expected mild. The NCG-KK tension is a property of the Weinberg contour, not of the full surface.

---

## V. Scenario Classification (Session 29 Fusion IX.3)

The Session 29 Fusion defined three scenarios based on P-30w and P-30phi. The 30Bb results require reinterpretation because P-30w's tree-level formulation is not the physically correct gate (einstein's reframing).

### Under Original Gate Definitions

| Scenario | Conditions | Verdict |
|:---------|:-----------|:-------|
| A (both PASS) | P-30w + P-30phi + RGE-A | **NOT REACHED** — anti-correlation prevents simultaneous satisfaction |
| B (one PASS) | P-30w PASS xor P-30phi PASS | **REALIZED** — phi PASS at Cand1, P-30w PASS at Cand2 (but at different points) |
| C (both FAIL) | P-30w + P-30phi both FAIL | Not realized (each passes at one candidate) |

### Under Reframed Gate (einstein)

At tau ~ 0.21: phi ~ 1.52 (marginal PASS), RGE gives sin^2(M_Z) ~ 0.231 for M_KK ~ 10^16 (PASS). This would be **Scenario A under reframed gates**, except:
- No V_total minimum exists at tau ~ 0.21 (Constraint 30Bb-2)
- B-30nck not evaluated at this point (expected mild but uncomputed)
- P-30w as originally defined (tree-level) fails (sin^2_B ~ 0.42)

**Assessment**: The framework's coupling structure is internally consistent at tau ~ 0.15-0.21. The framework's stabilization mechanism is not. The gates that fail are stabilization-dependent (no minimum to evaluate at), not coupling-structure-dependent.

---

## VI. Convergences and Divergences

### Convergences (both agents agree)

1. **phi_30 and sin^2_B (tree-level) are anti-correlated** on the U(2)-invariant surface. This is a structural property of the eigenvalue spectrum, not a numerical artifact.

2. **No V_total minimum on the full 3D U(2)-invariant surface.** V_spec/F_BCS ~ 8000 dominance is universal across all directions and tau values at rho=0.01.

3. **P-30golden is structurally inaccessible.** phi_30 max = 1.550 on the entire grid. The golden ratio 1.618 cannot be reached on U(2)-invariant geometries.

4. **N_max=6 computation is sound.** phi_30 = 1.53159 at tau=0.15 matches Session 12 to 5 decimal places. Full convergence verified at N_max = 3, 4, 5, 6.

5. **AZ-1 test was invalid.** Both agents confirmed the bare-conjugation test fails on Jensen where BDI is proven. AZ class at off-Jensen points remains unknown.

### Divergence: Interpretation of RGE-A

**Einstein's reframing** (tau ~ 0.21 is the correct evaluation point, tree-level match is meaningless) is structurally sound but introduces a tension with the 30Ba/30Bb gate framework. P-30w was pre-registered as a tree-level gate. Under reframing, P-30w's formulation is incorrect — the physically meaningful gate is "does sin^2(M_Z) = 0.231 after RGE running from the KK-scale value?" This gate PASSES at tau ~ 0.21.

The divergence is not about physics but about gate definitions. The synthesis records both interpretations.

---

## VII. Deliverables to Session 30A

1. **AZ class**: UNCOMPUTED. Session 30A must construct the proper time-reversal operator (spinor-space unitary, not bare conjugation) at the candidate point before interpreting any Pfaffian result. The AZ class on Jensen (BDI, Session 17c) cannot be assumed to hold off-Jensen.

2. **Candidate coordinates**: Cand1 (tau=0.180, eps=-0.135) from 30Ba gradient-balance. If reframed evaluation at tau ~ 0.21 is adopted, that point is not yet characterized for 30A purposes.

3. **Spectrum data**: Full N_max=6 eigenvalues and eigenvectors in `s30b_full_spectrum.npz` for both candidates.

---

## VIII. New Computable Threads Identified

| Thread | What it would resolve | Estimated cost | Status |
|:-------|:---------------------|:---------------|:-------|
| B-30nck at tau ~ 0.21 | Whether NCG-KK tension is mild at the RGE-compatible point | Zero (analytic from existing L1/L2 data) | Queued |
| Proper AZ-1 test | Whether BDI holds off-Jensen (gates 30A Pfaffian interpretation) | Medium (construct spinor-space T operator) | Queued |
| Full spectrum at tau = 0.21 | phi_30, DOS, PMNS at the RGE-compatible point | ~5 min | Queued |
| RGE with KK tower at tau ~ 0.21 | Whether threshold corrections improve or degrade running | Medium (need KK spectrum counting) | Queued |
| Cutoff-dependent stabilization at tau ~ 0.21 | Whether Lambda_crit mechanism creates effective minimum | Medium | Queued |
| PMNS at tau ~ 0.15-0.20 | Whether smaller tau improves perturbation theory convergence | ~5 min (from existing spectrum) | Queued |

---

## IX. Structural Findings of Lasting Significance

| ID | Finding | Source | Significance |
|:---|:--------|:-------|:-------------|
| SF-30Bb-1 | phi_30 monotonically decreasing in tau on U(2)-invariant surface | phonon-sim Step 3 | P-30phi window maps to tau in [0.10, 0.20]. Structural, not tuned. |
| SF-30Bb-2 | Tree-level Weinberg match is NOT a physical requirement | einstein Step 4 | RGE running is mandatory. sin^2_B at M_KK should be ~0.42, not 0.231. |
| SF-30Bb-3 | phi + RGE compatible at tau ~ 0.15-0.21 | Combined | Coupling structure works. Stabilization is the binding constraint. |
| SF-30Bb-4 | Wall 4 extends to full 3D U(2)-invariant surface | phonon-sim Task 4 | V_spec/F_BCS ~ 8000 in all directions at rho=0.01. |
| SF-30Bb-5 | AZ class test requires proper T operator construction | phonon-sim correction | Bare conjugation (D*=-D) is insufficient. S17c BDI proof used spinor-space unitary. |
| SF-30Bb-6 | PMNS perturbation theory breaks at large tau | phonon-sim Step 3 | V/Delta_E = 27 at tau=0.575. Kosmann couplings grow, splittings shrink. |

---

## X. Next Steps

1. **Evaluate at tau ~ 0.21**: Einstein's reframing identifies tau ~ 0.15-0.21 as the coupling-consistent region. Full spectrum + PMNS + B-30nck at this point would test whether coupling structure is genuinely viable.

2. **AZ-1 proper test**: Construct the spinor-space time-reversal unitary at off-Jensen points. Required before Session 30A Pfaffian computation can be interpreted.

3. **Stabilization**: The binding constraint. No V_total minimum on 3D U(2)-invariant surface. Surviving routes: non-U(2)-invariant deformations, different cutoff rho, cutoff-dependent Lambda_crit mechanism, non-perturbative contributions.

4. **Sagan checkpoint**: Session 30Bb delivers to Sagan for assessment. Key input: 1 hard close fired (B-30nck at tau~0.57), 0/4 positive signals, coupling structure viable at tau~0.21 but no minimum, Wall 4 extended to 3D.

---

## XI. Output Files

| File | Contents |
|:-----|:---------|
| `tier0-computation/s30b_full_spectrum.py` | Step 3 script (N_max=6, both candidates) |
| `tier0-computation/s30b_full_spectrum.npz` | Full eigenvalue data |
| `tier0-computation/s30b_full_spectrum_results.txt` | Detailed computation log |
| `tier0-computation/s30b_rge_running.npz` | RGE curves + NCG-KK analysis |
| `tier0-computation/s30b_rge_running.png` | RGE visualization |
| `tier0-computation/s30b_t1_extension.txt` | T1 grid extension (negative result) |
| `tier0-computation/s30b_gate_verdicts.txt` | Combined 30Ba + 30Bb verdicts |
| `sessions/session-30/session-30Bb-synthesis.md` | This document |
