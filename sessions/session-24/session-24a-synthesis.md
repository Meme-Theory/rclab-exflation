# Session 24a Synthesis: The Computation Sprint — Gate Verdicts

**Date**: 2026-02-21
**Session type**: COMPUTATION (7 cheap computations, all gates classified)
**Agents**: phonon-sim (phonon-exflation-sim, all computation), coordinator (gen-physicist, gate classification)
**Prior**: Panel 8% (range 6-10%), Sagan 5% (range 3-7%) -- post-Session 23
**Verdict**: **V-1 CLOSED. V_spec monotonically increasing. No stabilization minimum.**

---

## I. Gate Table

| Gate | Condition | Result | Verdict |
|:-----|:----------|:-------|:--------|
| **V-1** (V_spec Monotone) | No minimum at any rho | Monotonically increasing, all rho in [0.001, 0.5] | **CLOSED** |
| **V-3** (Min in [0.20, 0.40]) | tau_min in [0.20, 0.40] | No minimum anywhere | **FAIL** |
| **R-1** (Neutrino R in [17, 66]) | R in [17, 66] | R ~ 10^14 at all tau | **FAIL** |
| **AC-1** (Inconsistency > 5x) | Factor > 5 inconsistency | g1/g2 = 0.549 at tau=0.30 (SM-compatible) | **DOES NOT CLOSE** |
| Berry (diagnostic) | -- | Peak B = 982.5 at tau=0.10 | DIAGNOSTIC |
| Euclidean (diagnostic) | -- | I_E decreasing; round metric dominates | DIAGNOSTIC UNFAVORABLE |
| Eigenvalue ratios (diagnostic) | -- | Zero phi_paasch crossings | DIAGNOSTIC |

---

## II. Numbers

### II.1 V_spec(tau; rho) = -R_K(tau) + rho * [500*R_K^2 - 32*|Ric|^2 - 28*K]

Validation: R_K(0) = 2.000000 PASS.

| rho | V_spec(0) | V_spec(0.30) | V_spec(1.58) | Minimum |
|:----|:----------|:-------------|:-------------|:--------|
| 0.001 | -0.030 | 2.85 | 330.94 | NONE (monotone increasing) |
| 0.010 | 17.70 | 36.59 | 3555.33 | NONE |
| 0.050 | 96.50 | 190.33 | 17885.91 | NONE |
| 0.100 | 195.00 | 382.67 | 35799.14 | NONE |
| 0.500 | 983.00 | 1921.45 | 179104.96 | NONE |

Secondary scan (9 rho values in [0.001, 0.50]): ALL monotonically increasing. ZERO minima.

The a_4 curvature-squared combination (500*R_K^2 - 32*|Ric|^2 - 28*K) grows exponentially with tau and dominates the linear -R_K term at all positive rho. At tau=0, a_4_geom = 1970 while R_K = 2 -- a 1000:1 ratio. The Starobinsky R + R^2 competition does not produce a minimum because the R^2 term starts 1000x larger than R.

### II.2 Berry Curvature B_n(tau) = sum_{m!=n} |V_nm|^2 / (E_n - E_m)^2

| tau | B (gap-edge) |
|:----|:-------------|
| 0.00 | 0.000 |
| 0.10 | 982.49 |
| 0.15 | 600.58 |
| 0.20 | 468.21 |
| 0.25 | 418.02 |
| 0.30 | 407.15 |
| 0.35 | 421.28 |
| 0.40 | 455.56 |
| 0.50 | 583.66 |

Peak at tau=0.10. Local minimum at tau=0.30. Kramers symmetry confirmed. Magnitude ~1000x above pre-session estimate.

### II.3 Neutrino R = (m_3^2 - m_2^2)/(m_2^2 - m_1^2)

| tau | R | Gate [17, 66] |
|:----|:--|:--------------|
| 0.15 | 1.38e15 | FAIL |
| 0.20 | 2.17e14 | FAIL |
| 0.25 | 1.93e14 | FAIL |
| 0.30 | 5.44e14 | FAIL |
| 0.35 | 2.55e14 | FAIL |

Kramers degeneracy barely lifted. K_a cross-check at tau=0.30: R = 5.68 (finite but below gate lower bound).

### II.4 A/C Gauge-Gravity

| tau | tr(g_unit) | g1/g2 |
|:----|:-----------|:------|
| 0.15 | 8.596 | 0.741 |
| 0.20 | 8.929 | 0.670 |
| 0.25 | 9.334 | 0.607 |
| 0.30 | 9.813 | 0.549 |
| 0.35 | 10.369 | 0.497 |

g1/g2 = e^{-2tau} is the Session 17a structural identity. No factor-5 inconsistency. Full A/C check (kappa^2/(2*g_avg^2)) requires scale input not computed here.

### II.5 Euclidean Action I_E(tau) = -V_spec(tau)

I_E decreases (more negative) with tau at all rho >= 0.01. Round metric (tau=0) has highest I_E and dominates the Euclidean path integral. No Hawking-Page-type bounce.

### II.6 Eigenvalue Ratios

Zero phi_paasch crossings in (0,0) singlet at 0.1% or 1.0% tolerance. Closest approach: r_9(tau=0.50) = 1.376 (10.1% below phi_paasch = 1.53158). Session 12 phi result is inter-sector (m_{(3,0)}/m_{(0,0)}), not intra-sector.

---

## III. Probability Update

### III.1 Pre-Registered Outcome

Session 24a lands in the pre-registered scenario: **"V_spec monotone (V-1 closes)."**

| Outcome | Panel | Sagan |
|:--------|:------|:------|
| V_spec monotone (V-1 closes) | **5-7%** | **2-3%** |

R-1 FAIL compounds V-1 CLOSED but the pre-registered table already accounts for V-1 as the dominant closure. No additional reduction applied.

AC-1 not firing provides no uplift: gauge consistency is necessary but not sufficient when V_spec has no minimum.

### III.2 Trajectory

| Session | Panel | Sagan | Key Event |
|:--------|:------|:------|:----------|
| Pre-22 | 40% | 27% | -- |
| Post-22d | 40% | 27% | Clock closes rolling |
| Post-23a | 8% | 5% | K-1e BCS closure |
| **Post-24a** | **5-7%** | **2-3%** | **V-1 V_spec closure** |

---

## IV. What Was Tested

Seven computations ran. Total runtime: under 5 minutes. All inputs from existing data (Sessions 20a, 23a, 23c).

| Step | Computation | Lines of Code | Runtime | Gate |
|:-----|:-----------|:-------------|:--------|:-----|
| 1 | V_spec(tau; rho) | ~40 | < 1 min | V-1 CLOSED, V-3 FAIL |
| 2 | Berry curvature | ~20 | seconds | DIAGNOSTIC |
| 3 | Neutrino R | ~30 | seconds | R-1 FAIL |
| 4 | A/C gauge-gravity | analytic | -- | AC-1 DOES NOT CLOSE |
| 5 | Euclidean action | from Step 1 | 0 | DIAGNOSTIC UNFAVORABLE |
| 6 | Eigenvalue ratios | ~30 | seconds | DIAGNOSTIC |

---

## V. Output Files

| File | Producer |
|:-----|:---------|
| `tier0-computation/s24a_vspec.py` | phonon-sim |
| `tier0-computation/s24a_vspec.npz` | phonon-sim |
| `tier0-computation/s24a_vspec.png` | phonon-sim |
| `tier0-computation/s24a_berry.py` | phonon-sim |
| `tier0-computation/s24a_berry.npz` | phonon-sim |
| `tier0-computation/s24a_berry.png` | phonon-sim |
| `tier0-computation/s24a_neutrino.py` | phonon-sim |
| `tier0-computation/s24a_neutrino.txt` | phonon-sim |
| `tier0-computation/s24a_eigenvalue_ratios.py` | phonon-sim |
| `tier0-computation/s24a_eigenvalue_ratios.npz` | phonon-sim |
| `tier0-computation/s24a_eigenvalue_ratios.png` | phonon-sim |
| `tier0-computation/s24a_gate_verdicts.txt` | coordinator |
| `sessions/session-24/session-24a-synthesis.md` | coordinator |

---

*Session 24a synthesis assembled by coordinator (gen-physicist) from phonon-sim (phonon-exflation-sim) computation results. All gate classifications applied against pre-registered thresholds from Session 24a prompt Section IV. No interpretation -- numbers and classifications only. Interpretation deferred to Session 24b.*
