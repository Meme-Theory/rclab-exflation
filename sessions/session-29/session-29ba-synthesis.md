# Session 29Ba Synthesis: 3-Sector Depth + PMNS Extraction

**Date**: 2026-02-28
**Session type**: COMPUTATION (3 pre-registered gates + 2 structural checks)
**Agents**: phonon-sim (phonon-exflation-sim, computation), neutrino (neutrino-detection-specialist, physics assessment), coordinator (gate classification + synthesis)
**Depends on**: Session 28 fusion synthesis, Session 23a (Kosmann singlet), Session 27 (multi-sector BCS)
**Independent of**: Session 29A (KC-3/backreaction results not required)

---

## I. Session Overview

Session 29Ba addressed three computations from the Session 29B plan that have NO dependency on Session 29A results:

| Computation | Description | Cost | Gate |
|:------------|:-----------|:-----|:-----|
| 29B-1 | 3-sector F_BCS^{eff} | Zero-cost (post-processing s27 data) | B-29a / P-29a |
| 29B-6 | 3-sector gradient balance | Zero-cost (downstream of 29B-1) | P-29a extension |
| 29B-2 | Tridiagonal PMNS extraction | Low-cost (3x3 diagonalization) | B-29b / P-29b |

All three produce results with standalone mathematical value regardless of the KC-3 verdict from Session 29A.

**Result**: 0/2 hard closes fired. 3/3 positive signals fired (one conditionally). The 3-sector stabilization mechanism is confirmed with large margins. The PMNS extraction produces a conditional theta_13 match but fails the full mixing angle picture.

---

## II. 29B-1: 3-Sector F_BCS^{eff}

### II.1 Computation

The BCS free energy was restricted to the 3 permanently supercritical sectors identified by the LZ retraction (Session 28 fusion synthesis XS-6):

- **(0,0)**: Peter-Weyl multiplicity 1, always supercritical at mu = lambda_min
- **(3,0)**: multiplicity 100, first-order (L-9, cubic invariant c = 0.00552)
- **(0,3)**: multiplicity 100, first-order (L-9, cubic invariant c = 0.00723)

F_BCS^{3-sector}(tau, mu) = sum_{r in {(0,0),(3,0),(0,3)}} mult(r) * F_cond^{(r)}(tau, mu)

Computed over the full (tau, mu) grid: 9 tau values in [0, 0.50], 12 mu/lambda_min values in [0, 3.0].

### II.2 Results

**Global 3-sector minimum**: F_3sect = -17.2217 at (tau = 0.35, mu/lambda_min = 1.20)

**Hessian at minimum**: eigenvalues [1086.01, 6567.61] -- both strongly positive. **Genuine minimum confirmed.**

**Comparison to full-sector**:
- At the same grid point (tau=0.35, mu/lmin=1.20): F_full = -18.56, F_3sect/F_full = 0.928 (92.8%). Load-bearing sectors carry nearly all condensation energy at this chemical potential.
- At the global full-sector minimum (F_full = -127.10 at a deeper mu): F_3sect/F_full = 0.136 (13.6%). Re-entrant sectors dominate at high mu.

**Multiplicity note**: The computation used Peter-Weyl multiplicities (1, 100, 100), consistent with the s27/s28 convention where F_cond already integrates over the Dirac eigenvalues within each sector. The prompt's mult=16 for (0,0) would double-count the 16 singlet eigenvalues.

### II.3 Gate Verdicts

**Constraint B-29a** (F_BCS^{3-sector} < 0.1 at ALL (tau, mu)): **DOES NOT FIRE.**
|F_3sect| = 17.22 exceeds the threshold by factor 172x. The B-3 depth condition is satisfied by the permanently supercritical sectors alone.

**Implication**: The L-8 non-convergence (482% growth from p+q<=3 to p+q<=4) is irrelevant for stabilization. The 3-sector sum is finite, computable, and UV-safe.

**Surviving solution space**: Stabilization confirmed with the permanent sectors. The L-8 divergence problem remains open ONLY for full-sector quantities (cosmological constant, total condensation energy).

**P-29a** (F_3sect > 0.1 with genuine minimum): **FIRES.**
3-sector stabilization confirmed with Hessian verification. This is the computational confirmation of fusion XS-6.

### II.4 Hessian Structure Across mu

| mu/lmin | F_3sect at min | tau_min | Hessian eigvals | Genuine? |
|:--------|:--------------|:--------|:---------------|:---------|
| 0.95 | -0.020 | 0.50 | [-1313, -1.2] | No |
| 1.00 | -11.50 | 0.00 | [-1504, 9203] | No (saddle) |
| 1.05 | -7.28 | 0.50 | [325, 4494] | Yes |
| 1.10 | -1.03 | 0.15 | [403, 817] | Yes |
| 1.20 | -17.22 | 0.35 | [1086, 6568] | Yes |
| 1.50 | -3.72 | 0.35 | [-94, 1880] | No (saddle) |

Genuine minima exist at mu/lmin = 1.05, 1.10, and 1.20. The deepest genuine minimum is at mu/lmin = 1.20 (tau = 0.35), coinciding with the Session 27 S-3 interior minimum.

---

## III. 29B-6: 3-Sector Gradient Balance

### III.1 Computation

The gradient balance condition: S_b'(tau_0) + F_BCS^{3-sector}'(tau_0) = 0

S_b(tau) loaded from `s24a_vspec.npz`. F_BCS^{3-sector}(tau) from the 29B-1 output. Both differentiated by finite differences.

Lambda_crit computed as: Lambda_crit = (|F_BCS''| / |S_b''|)^{1/6}, measuring the cutoff scale at which the spectral action perturbation balances the BCS gradient.

### III.2 Results

At mu/lmin = 1.20 (the Hessian-confirmed minimum):

| tau_0 | Lambda_crit | In [0.20, 0.50]? | O(1)? |
|:------|:-----------|:-----------------|:------|
| 0.25 | 0.995 | Yes | Yes |
| 0.30 | 0.783 | Yes | Yes |

Additional balance points at other mu values:

| mu/lmin | tau_0 range | Lambda_crit range |
|:--------|:-----------|:-----------------|
| 1.00 | 0.50 | 9.67 |
| 1.05 | 0.30-0.40 | 4.00-7.50 |
| 1.10 | 0.10 | 1.33 |
| 1.20 | 0.25-0.30 | 0.78-1.00 |
| 1.50 | 0.25-0.30 | 3.46-5.55 |

### III.3 Gate Verdict

**P-29a extension** (tau_0 in [0.20, 0.50] with Lambda_crit = O(1)): **FIRES.**

The gradient balance holds at tau_0 = 0.25-0.30 with Lambda_crit ~ 0.8-1.0 at the physically relevant mu/lmin = 1.20. This confirms the fusion XS-8 estimate (Lambda_crit ~ 3.0 for full-sector; the 3-sector restriction produces a LOWER Lambda_crit because the BCS curvature is concentrated in fewer sectors).

**Implication**: Natural stabilization at the compactification scale Lambda ~ O(1). No fine-tuning required. The spectral action slope S_b'(tau) starts at zero (round metric is Einstein) and grows linearly, while F_BCS' peaks at the BCS minimum. Their balance occurs naturally in the physical window.

---

## IV. 29B-2: Tridiagonal PMNS Extraction

### IV.1 Computation

The effective mass matrix in the (0,0) singlet sector:

H_eff = diag(E_1, E_2, E_3) + V_pairing

where E_1, E_2, E_3 are the three distinct positive-energy eigenvalue levels (multiplicities 1, 4, 3 = the 2+8+6 splitting from Session 24a), and V_pairing is the Kosmann pairing matrix from Session 23a.

Three methods tested:
- **Method B**: Degenerate perturbation theory -- average V_pairing within each degenerate multiplet, reduce to 3x3 H_eff, diagonalize. Eigenvalues match full 16x16 to 0.04% at all tau. **This is the physically correct reduction.**
- **Method C**: Single-mode (one representative per level). Wrong by 10-20%.
- **Full 16x16**: Reference diagonalization of the complete singlet H_eff.

PMNS angles extracted from the 3x3 eigenvector matrix U:
- sin^2(theta_13) = |U_{e3}|^2
- tan^2(theta_12) = |U_{e2}|^2 / |U_{e1}|^2
- tan^2(theta_23) = |U_{mu3}|^2 / |U_{tau3}|^2
- R = (m_3^2 - m_2^2) / (m_2^2 - m_1^2)

### IV.2 Results (Method B)

| tau | sin^2(theta_13) | theta_12 (deg) | theta_23 (deg) | R | V_12 | V_23 |
|:----|:---------------|:--------------|:--------------|:--|:-----|:-----|
| 0.10 | 0.299 | 34.6 | 54.7 | 0.63 | 0.140 | 0.065 |
| 0.15 | 0.254 | 35.1 | 48.8 | 0.48 | 0.149 | 0.062 |
| 0.20 | 0.203 | 36.5 | 42.0 | 0.38 | 0.160 | 0.059 |
| 0.25 | 0.150 | 38.3 | 35.0 | 0.33 | 0.172 | 0.056 |
| 0.30 | 0.105 | 39.9 | 28.7 | 0.30 | 0.186 | 0.053 |
| 0.35 | 0.072 | 41.0 | 23.4 | 0.30 | 0.202 | 0.050 |
| 0.40 | 0.050 | 41.8 | 19.4 | 0.29 | 0.220 | 0.047 |
| 0.50 | 0.027 | 42.7 | 14.0 | 0.29 | 0.262 | 0.042 |

PDG reference: sin^2(theta_13) = 0.0218, theta_12 = 33.44 deg, theta_23 = 49.1 deg, R = 32.6

### IV.3 Selection Rules (Structurally Permanent)

Confirmed at all tau > 0 to machine precision:

| Coupling | Value | Comment |
|:---------|:------|:--------|
| V(L1, L2) | 0.140-0.262 | Nearest-neighbor, growing with tau |
| V(L1, L3) | 0 EXACTLY | Selection rule (anti-Hermiticity + orthogonality) |
| V(L2, L3) | 0.042-0.065 | Nearest-neighbor, decreasing with tau |
| V(L1, L1), V(L2, L2), V(L3, L3) | 0 EXACTLY | Within-level forbidden |

The tridiagonal structure is an exact consequence of the Kosmann operator's anti-Hermiticity and the orthogonality of degenerate eigenstates. This is structurally permanent: it holds for ANY left-invariant metric on SU(3) with the Jensen deformation.

### IV.4 Gate Verdicts

**Constraint B-29b** (sin^2(theta_13) < 0.005 or > 0.10 at ALL tau): **DOES NOT FIRE.**
sin^2(theta_13) enters the allowed range [0.005, 0.10] at tau >= 0.35. The tridiagonal structure does not universally fail.

**Implication**: The particle physics prediction program is NOT fully closed by this test.

**Surviving solution space**: The tridiagonal PMNS structure produces viable sin^2(theta_13) at large tau. Full PMNS fit requires mode-dependent BCS dressing (escape route identified in the 29B plan).

**P-29b** (sin^2(theta_13) in [0.015, 0.030]): **FIRES CONDITIONALLY at tau = 0.50.**
sin^2(theta_13) = 0.027 at tau = 0.50 (PDG: 0.022, within 23%). However:
- theta_12 = 42.7 deg (PDG: 33.4, 28% too high)
- theta_23 = 14.0 deg (PDG: 49.1, factor 3.5x too low)
- R = 0.29 (PDG: 32.6, factor 112x too low -- confirms N-01/N-03)

### IV.5 Physics Assessment (from neutrino-detection-specialist)

**Root cause of partial failure**: V_12/dE_12 ~ 6-9 across the tau range. The L1-L2 coupling is much larger than their level splitting, placing the system in the strong-mixing regime. At tau = 0.50: V_12 = 0.262, dE_12 = E_2 - E_1 = 0.030, ratio = 8.7. This has three consequences:

(a) **R is crushed**: The mass eigenvalue m_1 is pushed far below E_1 by strong L1-L2 repulsion. The resulting mass-squared differences dm^2_21 ~ dm^2_32, giving R ~ 0.3 instead of 33. The experimental R = 33 requires a hierarchy between the two splittings, which demands either weak coupling or very unequal level spacings. Neither condition is met.

(b) **theta_13 and theta_23 trade off**: As tau increases, V_12/dE_12 grows and theta_13 decreases (good) but theta_23 simultaneously collapses (bad). At the tau where theta_13 matches PDG (tau ~ 0.50), theta_23 = 14 deg instead of 49 deg. There is no tau value where all three angles simultaneously match.

(c) **theta_12 is systematically high**: theta_12 ~ 35-43 deg across all tau, vs PDG 33.4 deg. At tau = 0.10 it is closest (34.6 deg) but at that tau sin^2(theta_13) = 0.30 (14x too large).

**Structural success**: The correct hierarchy (theta_12 >> theta_13) emerges naturally from V(L1,L3) = 0. The selection rule forces theta_13 to be generated only through the L1-L2-L3 chain, not directly. This is qualitatively the same mechanism as in the Standard Model's PMNS matrix, where theta_13 is the smallest angle. In the neutrino model-building literature, this resembles the "nearest-neighbor interaction" (NNI) texture ansatz -- here it is DERIVED from the Peter-Weyl structure of the Kosmann derivative rather than postulated.

**Structural limitation**: The tridiagonal constraint is TOO restrictive for simultaneous 3-angle fitting. A general 3x3 unitary has 3 angles and 1 phase (4 parameters). The tridiagonal H_eff has only 2 free parameters (V_12 and V_23, with V_13 = 0 fixed). Two parameters cannot fit four observables.

**theta_12 AND condition caveat**: The Session 29Ba prompt defines P-29b as sin^2(theta_13) in [0.015, 0.030] only. However, the broader pre-registered PMNS gate (from neutrino's gate registry) includes theta_12 in [28, 38] deg as an AND condition. At tau = 0.50 where theta_13 passes, theta_12 = 42.8 deg -- OUTSIDE [28, 38]. Under the narrower prompt gate: CONDITIONAL PASS. Under the broader gate with theta_12 AND condition: FAIL. Both framings are reported for completeness.

**Escape route**: Mode-dependent BCS gap Delta_n from solving the full BdG equation within the (0,0) singlet. Non-uniform dressing breaks the strict degeneracy averaging and effectively introduces V_13 != 0 corrections. Whether this shifts theta_23 toward maximal mixing is computable but requires the 29B-3 Bogoliubov BCS computation (Session 29Bb).

---

## V. Combined Gate Verdicts

| Gate | Type | Computation | Condition | Result | Verdict |
|:-----|:-----|:-----------|:----------|:-------|:--------|
| B-29a | Hard close | 29B-1 | F_3sect < 0.1 at ALL (tau, mu) | F_3sect = -17.22, Hessian [1086, 6568] | **PASS** (172x margin) |
| B-29b | Hard close | 29B-2 | sin^2(theta_13) < 0.005 or > 0.10 at ALL tau | 0.027-0.072 at tau = 0.35-0.50 | **PASS** |
| P-29a | Positive | 29B-1 | F_3sect > 0.1, genuine minimum | Confirmed | **FIRES** |
| P-29a ext | Positive | 29B-6 | tau_0 in [0.20, 0.50], Lambda_crit = O(1) | tau_0 = 0.25-0.30, Lambda_crit = 0.78-1.00 | **FIRES** |
| P-29b | Positive | 29B-2 | sin^2(theta_13) in [0.015, 0.030] | 0.027 at tau = 0.50 | **FIRES (conditional)** |

**P-29b caveat**: Under the broader pre-registered PMNS gate (which includes theta_12 in [28, 38] as an AND condition), P-29b FAILS -- theta_12 = 42.8 deg at the tau where theta_13 passes. The Session 29Ba prompt tests only sin^2(theta_13), under which it conditionally passes. Both framings recorded.

**Session score**: 0/2 hard closes fired. 3/3 positive signals fired (one conditional, with theta_12 caveat).

---

## VI. Framework Implications

### VI.1 3-Sector Stabilization (29B-1 + 29B-6)

The computational confirmation of fusion XS-6 is the cleanest result of this session. The 3 permanently supercritical sectors provide:

1. **Sufficient depth**: |F_3sect| = 17.22 >> 0.1 (B-3 threshold satisfied by 172x)
2. **Genuine minimum**: Both Hessian eigenvalues strongly positive at (tau=0.35, mu/lmin=1.20)
3. **Natural gradient balance**: Lambda_crit ~ 1.0 at tau = 0.25-0.30, confirming no fine-tuning
4. **UV-safety**: Finite sum over 201 modes (1 + 100 + 100), immune to L-8 divergence

The framework splits cleanly into two regimes:
- **Stabilization**: finite, computable, UV-safe (3-sector F_BCS^{eff}). CONFIRMED.
- **Cosmological constant**: divergent, requiring renormalization (full-sector sum). OPEN.

This resolves the L-8 tension raised in Session 28 (fusion UT-4) for the stabilization problem. The re-entrant sectors contribute additional condensation energy at high mu but are NOT required for modulus trapping.

### VI.2 PMNS Extraction (29B-2)

The tridiagonal PMNS result is a structural partial success:

**What works**:
- sin^2(theta_13) reaches the PDG window at large tau (0.027 at tau=0.50 vs PDG 0.022)
- The correct hierarchy theta_12 >> theta_13 emerges from V(L1,L3) = 0
- Method B (degenerate perturbation theory) is validated against the full 16x16

**What fails**:
- theta_23 collapses to 14 deg at the tau where theta_13 matches (PDG: 49.1 deg)
- theta_12 is systematically 28% too high (42.7 vs 33.4 deg)
- R ~ 0.29, confirming the known 112x shortfall (N-01/N-03)
- The pass occurs at tau = 0.50, outside the expected BCS stabilization range (0.20-0.40)

**Structural insight**: The tridiagonal constraint (2 free parameters for 4 observables) is too restrictive for a simultaneous 3-angle fit. The system is in the strong-mixing regime where V_12/dE_12 ~ 6-9, preventing independent angle tuning.

**Assessment**: The P-29b conditional pass should be recorded honestly: the specific pre-registered gate (sin^2(theta_13) in [0.015, 0.030]) is satisfied, but the broader PMNS picture is a quantitative failure. This continues the pattern from Session 28 FP-5: the particle physics prediction program has largely failed, with permanent structural results (selection rules, hierarchy) surviving but quantitative predictions not matching PDG values.

### VI.3 Constraint Map Updates

**Constraint [B-29a]**: F_BCS^{3-sector} = -17.22 at genuine minimum. **Source**: 29B-1, s29b_3sector_fbcs.npz. **Implication**: Stabilization does NOT require re-entrant sectors. L-8 divergence is irrelevant for modulus trapping. **Surviving solution space**: All mechanisms that use 3-sector F_BCS for stabilization remain viable.

**Constraint [B-29b]**: sin^2(theta_13) in [0.027, 0.072] at tau = [0.35, 0.50]. **Source**: 29B-2, s29b_pmns_extraction.npz. **Implication**: Tridiagonal PMNS does not universally fail. theta_13 is viable; theta_23 and R are not. **Surviving solution space**: Mode-dependent BCS dressing (29B-3) as escape route for theta_23. R-failure confirmed as structural (N-01/N-03).

### VI.4 Computable Threads Identified

1. **Mode-dependent BdG within (0,0) singlet**: Solve Delta_n self-consistently with the tridiagonal V_{nm}. Tests whether non-uniform gap breaks the theta_13/theta_23 trade-off. Requires 29B-3 Bogoliubov BCS computation. **Status**: queued for Session 29Bb.

2. **PMNS at the physical tau**: The P-29b pass occurs at tau = 0.50. If the BCS minimum is at tau = 0.35 (from 29B-1 Hessian), the physical PMNS angles are at tau = 0.35: sin^2(theta_13) = 0.072, outside the P-29b window. The pass requires tau >= 0.45. The 29A backreaction trajectory (t_BCS at tau ~ 0.50) would need to set the physical tau. **Status**: depends on 29A results integration.

---

## VII. Output Files

| File | Description |
|:-----|:-----------|
| `tier0-computation/s29b_3sector_fbcs.py` | 3-sector F_BCS computation + gradient balance |
| `tier0-computation/s29b_3sector_fbcs.npz` | Full results: F_3sect grid, Hessians, gradient balance |
| `tier0-computation/s29b_3sector_fbcs.png` | 3-panel plot: F_3sect(tau), fraction, gradient balance |
| `tier0-computation/s29b_pmns_extraction.py` | PMNS extraction (Methods B and C) |
| `tier0-computation/s29b_pmns_extraction.npz` | Full results: mixing angles, eigenvalues, U matrices |
| `tier0-computation/s29b_pmns_extraction.png` | 4-panel diagnostic: theta_13, theta_12, theta_23, R vs tau |
| `tier0-computation/s29b_pmns_extraction.txt` | Human-readable results summary |
| `tier0-computation/s29b_gate_verdicts.txt` | Gate verdicts (appended to 29Ab verdicts) |

---

*Synthesis written by coordinator. Gate classification performed BEFORE interpretation per computation discipline. All numbers verified against .npz output files. Computation by phonon-sim (phonon-exflation-sim). Physics assessment by neutrino (neutrino-detection-specialist). Notation follows sessions/framework/MathVariables.md.*
