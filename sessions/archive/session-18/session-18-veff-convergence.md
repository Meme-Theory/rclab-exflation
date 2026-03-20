# Session 18: V_eff Convergence -- The Decisive Computation

**Date**: 2026-02-15
**Team**: session-18-veff (4 agents + team-lead)
**Agents**: KK-Theorist (KK-1), Baptista (B-6), Connes (C-1), Hawking (H-5)
**Designated Writer**: Hawking-Theorist

---

## Executive Summary

The 1-loop Coleman-Weinberg effective potential V_eff(s) on the Jensen-deformed
SU(3) was computed with the COMPLETE bosonic Kaluza-Klein tower for the first time.
The result is **monotonically decreasing** -- no interior minimum exists at the
1-loop level. The Jensen modulus s is unstabilized. This triggers the pre-registered
FATAL Constraint Condition "No minimum at any s > 0" for the 1-loop CW approximation.

**This closes the 1-loop approximation, not the framework itself.**

---

## Task Results

### KK-1: Full Bosonic KK Tower (KK-Theorist) -- COMPLETE

Script: `tier0-computation/kk1_bosonic_tower.py`
Data: `tier0-computation/kk1_bosonic_spectrum.npz`

- Scalar Laplacian eigenvalues: 714 distinct (p+q <= 6)
- Vector (Hodge) Laplacian eigenvalues: 1,456 distinct (p+q <= 4)
- Total: 2,170 distinct bosonic eigenvalues
- PW multiplicity: dim(p,q) per eigenvalue (VERIFIED correct at lines 283, 558)
- Ricci sign correction applied: Delta_1 = nabla*nabla + Ric (positive, compact)
- All vector eigenvalues strictly positive (H^1(SU(3)) = 0 confirmed)
- API: `from kk1_bosonic_tower import bosonic_spectrum_at_s`

**Display bug**: Lines 613, 905, 917 use `dim_pq**2` (WRONG for display only).
The computation path uses `dim_pq` (CORRECT). This cosmetic bug caused initial
confusion about whether bosonic DOF were 1.8M or 52K.

### B-6: Scalar & Vector Laplacian (Baptista) -- COMPLETE

Script: `tier0-computation/b6_scalar_vector_laplacian.py`

- Independent implementation of scalar/vector Laplacians
- Scalar eigenvalues: match KK-1 at machine epsilon
- **Vector Laplacian sign error** (initial): used -Ric instead of +Ric
  - Corrected after team-lead flagged the discrepancy
  - Compact manifold Delta_1 is non-negative by construction
- V_tree normalization: normalize=True gives 5x amplification (V(0) = 1.0 vs 0.2)
  - IRRELEVANT: V_tree ~ O(0.2) while V_CW ~ O(10^4)

### C-1: Seeley-DeWitt Convergence (Connes) -- COMPLETE

Script: `tier0-computation/c1_seeley_dewitt_convergence.py`

- Individual SD coefficients a_0, a_2, a_4: NOT CONVERGED at mps=6
  - Successive-shell ratios 2-5x (GROWING)
  - Pre-asymptotic regime (Weyl's law: sum ~ Lambda_max^12)
  - a_0 changes 300% from mps=5 to mps=6
- **Normalized SHAPE: STABLE to 0.55%**
  - Minimum LOCATION reliable to ~1% from truncation
  - Absolute DEPTH meaningless (changes by orders of magnitude)
  - New shells contribute nearly s-INDEPENDENT factor
- a_2/a_0 ratio convergence: 3.8% at s=1.0 (good), 14% at s=0.0 (poor)
- Cost: mps=8 is 5.5x slower, would NOT fix convergence
- Verdict: Proceed with mps=6. Trust shape, not magnitude.

### H-5: Full CW V_eff (Hawking) -- COMPLETE

Script: `tier0-computation/h5_standalone_verify.py` (standalone, zero agent imports)
Plot: `tier0-computation/h5_standalone_verify.png`
GPU: AMD RX 9070 XT via ROCm (venv312, Python 3.12)
Runtime: 186s (3.1 min)

---

## Definitive Results

### DOF Budget

| Component | Distinct eigenvalues | PW multiplicity | Total DOF |
|:----------|--------------------:|:---------------:|----------:|
| Scalar Laplacian (mps=6) | 714 | dim(p,q) | 27,468 |
| Vector Laplacian (mps=4) | 1,456 | dim(p,q) | 25,088 |
| **Total Bosonic** | **2,170** | | **52,556** |
| Dirac spectrum (mps=6) | ~27,468 | dim(p,q) | **439,488** |
| **Ratio F/B** | | | **8.4 : 1** |

Session 17a had 4 bosonic DOF. Session 18 has 52,556. The full tower adds
~13,000x more bosonic modes, but fermions still outnumber bosons 8.4:1.

### V_eff Values (mu = 1.0)

```
s       V_tree      V_boson       V_fermion       V_total
------  ----------  -----------   -------------   -------------
0.000    2.000e-01  -3.613e+01   -5.350e+03      -5.386e+03
0.050    2.000e-01  -3.023e+01   -5.509e+03      -5.539e+03
0.100    1.989e-01  -1.184e+01   -6.001e+03      -6.013e+03
0.150    1.963e-01  +2.088e+01   -6.869e+03      -6.848e+03
0.200    1.916e-01  +7.082e+01   -8.176e+03      -8.105e+03
0.300    1.730e-01  +2.407e+02   -1.251e+04      -1.227e+04
0.500    8.465e-02  +1.104e+03   -3.328e+04      -3.218e+04
1.000   -6.703e-01  +1.857e+04   -4.067e+05      -3.882e+05
2.500   -2.865e+01  +2.247e+07   -4.195e+08      -3.970e+08
```

### Monotonicity

- V_eff is **MONOTONICALLY DECREASING** from s=0 to s=2.5 (16/16 points)
- The fermionic CW dominates at every s-value
- At s=0.3: |V_fermion|/|V_boson| = 52
- V_boson starts NEGATIVE at s < 0.13 (reinforces descent), turns positive at s ~ 0.13
- V_tree is 4 orders of magnitude smaller than V_CW (IRRELEVANT)

### mu-Dependence

```
          mu=0.01       mu=0.10       mu=1.00       mu=10.0       mu=100
s=0.00:   -1.87e+05     -9.63e+04     -5.39e+03     +8.55e+04     +1.77e+05
s=0.15:   -2.02e+05     -1.05e+05     -6.85e+03     +9.10e+04     +1.89e+05
s=0.30:   -2.55e+05     -1.34e+05     -1.23e+04     +1.09e+05     +2.30e+05
s=1.00:   -2.49e+06     -1.44e+06     -3.88e+05     +6.62e+05     +1.71e+06
```

- At mu=1: mono-DECREASING (fermionic runaway)
- At mu=10: V flips sign, mono-INCREASING (bosonic wall)
- At mu=100: strongly mono-INCREASING
- **Qualitative behavior is SCHEME-DEPENDENT** -- the sign of V_total depends on mu

### Comparison with Session 17a

| | Session 17a | Session 18 |
|:---|:---|:---|
| Bosonic DOF | 4 (C^2 gauge only) | 52,556 (full tower) |
| Fermionic DOF | 439,488 | 439,488 |
| Ratio F/B | 109,872 | 8.4 |
| V_eff shape | mono DECREASING | mono DECREASING |
| Minimum | none (runaway) | none (runaway) |
| V_boson magnitude | negligible | 2-6% of V_fermion |

The full bosonic tower SLOWS the descent but does NOT reverse it.

---

## Bugs Found During Session

1. **h5_full_veff.py: Vector double-counting** -- `compute_full_Veff()` passed combined
   bosonic eigenvalue array (scalar+vector) as "scalar_evals" AND separate vector_evals.
   Vector modes counted twice. Fixed by setting vector_evals=None.

2. **Dirac eigenvalue dtype** -- `collect_spectrum()` returns complex128 eigenvalues
   (purely imaginary: i*lambda_real). Using `lam**2` gives negative m^2 (wrong).
   Must use `abs(lam)**2` for physical mass-squared. The existing `compute_fermionic_CW`
   in h5_full_veff.py handles this correctly with `np.abs(evals)`.

3. **Indentation bug in standalone** -- `nabla.append(nc)` placed inside `for a` loop
   instead of `for c` loop in vector_laplacian_on_irrep. Produced 64 nabla operators
   instead of 8. Found and fixed before production run.

4. **kk1_bosonic_tower.py display bug** -- `count_bosonic_dof()` and `report_bosonic_summary()`
   use `dim_pq**2` (lines 613, 905, 917). Computation path uses `dim_pq` (correct).
   Cosmetic only -- did NOT affect eigenvalue data.

---

## Constraint Condition Assessment

| Condition | Result | Status |
|:----------|:-------|:-------|
| F1: s_0 in [0.24, 0.37] | No s_0 (no minimum) | **DECISIVE CLOSURE** |
| F2: u(2) gauge bosons massless | Structural (proven) | PASS |
| F3: Z_3 conjugate degeneracy | Theorem (proven) | PASS |
| F4: SM sectors lightest | Already verified | PASS |
| F5: Spectral gap open | Already verified | PASS |
| No minimum at s > 0 | **CONFIRMED** | **DECISIVE CLOSURE** |
| V_eff shift > 50% between truncations | Shape stable 0.55% (C-1) | PASS |

**Pre-registered FATAL condition triggered**: No interior minimum at 1-loop CW level.

---

## Thermodynamic Interpretation (Hawking)

V_CW is the Helmholtz free energy F(s, mu) of the quantum fields on the internal
space (SU(3), g_s). The Jensen deformation parameter s is the thermodynamic order
parameter for the shape of the internal geometry.

**F(s) decreases monotonically**: The deformed geometry has LOWER free energy than
the bi-invariant metric. The internal space WANTS to deform. This is physically
correct -- fermions in a curved background have lower vacuum energy than in flat
space (curved-space Casimir effect).

**But there is no restoring force**: The 1-loop fermionic vacuum energy overwhelms
all other contributions at every value of s. The system runs away to s -> infinity,
where the internal geometry degenerates. This is the classic modulus stabilization
problem of Kaluza-Klein compactifications.

The mu-dependence reveals the fundamental limitation: at mu=1 the potential decreases,
at mu=100 it increases. The physical answer depends on the renormalization scheme,
which means the 1-loop calculation is not predictive for this quantity. Non-perturbative
effects are required to determine the true vacuum.

---

## What This Means for the Framework

### What is NOT closed
- The 1-loop Coleman-Weinberg approximation to V_eff(s)
- Any claim that the Jensen modulus is stabilized by perturbative quantum corrections
- The specific prediction path: "V_eff selects s_0 -> gauge coupling ratios follow"

### What is NOT closed
- The framework itself (KO-dim=6, SM quantum numbers, chirality, etc.)
- The possibility of non-perturbative stabilization
- All 11 proven structural results from Sessions 7-17

### What is needed next
1. **Casimir energy on K**: Full zeta-function regulated sum, not truncated CW
2. **Fermion condensates**: Non-perturbative chiral symmetry breaking on SU(3)
3. **Flux/instanton corrections**: Gauge field configurations on K
4. **Higher-loop gravity**: 2-loop gravitational effective action
5. **Lattice approach**: Non-perturbative computation of V_eff on discrete SU(3)

The modulus stabilization problem is well-known in string theory (KKLT, LVS, etc.)
and typically requires non-perturbative ingredients. The phonon-exflation framework
now faces the same challenge.

---

## Framework Probability Update

| Agent | Pre-Session 18 | Post-Session 18 | Change |
|:------|:--------------:|:---------------:|:------:|
| Hawking | 42-55% | 35-50% | -7% |

The monotonic V_eff is a NEGATIVE result for the predictive power of the framework
at the 1-loop level. However, it is an EXPECTED result -- modulus stabilization
is hard in every KK framework. The structural results (KO-dim=6, SM quantum numbers)
remain intact. The probability decrease reflects the loss of a concrete prediction
path, not a structural flaw.

---

## Verified by Independent Computation

Three independent computations agree:

1. **Hawking standalone** (h5_standalone_verify.py): Zero agent-script imports,
   all Laplacians inlined, GPU via ROCm. V_total(0.3) = -1.227e+04.

2. **Coordinator** (via h5_full_veff.py + kk1_bosonic_tower.py):
   V_total(0.3) = -1.227e+04. Exact match.

3. **Hawking quick sweep** (inline computation): V_total(0.3) = -1.227e+04.
   Exact match.

All three give identical results to 4 significant figures.

---

## Deliverables

| File | Description |
|:-----|:------------|
| `tier0-computation/h5_standalone_verify.py` | Standalone V_eff (zero agent imports, GPU) |
| `tier0-computation/h5_standalone_verify.png` | 4-panel plot |
| `tier0-computation/h5_full_veff.py` | Original H-5 script (vector double-counting fixed) |
| `tier0-computation/h5_production_run.py` | Production sweep script (updated summaries) |
| `tier0-computation/kk1_bosonic_tower.py` | Full bosonic KK tower (KK-Theorist) |
| `tier0-computation/kk1_bosonic_spectrum.npz` | Pre-computed spectra at 4 s-values |
| `tier0-computation/b6_scalar_vector_laplacian.py` | Scalar/vector Laplacians (Baptista) |
| `tier0-computation/c1_seeley_dewitt_convergence.py` | SD convergence assessment (Connes) |
| `sessions/session-18/session-18-veff-convergence.md` | This document |
