# Session 41 Plan: Spectral Refinement and the Constants

**Date**: 2026-03-11
**Author**: PI + team-lead
**Format**: Mixed — parallel computations (W1-W2) + directed conceptual exploration (W3)
**Source**: Session 40 structural cartography, S40 addenda (13 documents), PI directive on spectral refinement cosmology
**Motivation**: Session 40 completed the structural cartography (27 closures, 28D positive Hessian, compound nucleus dissolution). The S40 addenda unified the framework around the static phononic crystal substrate picture. The PI now directs: the early universe was not hot and dense — it was coarse-grained. Expansion is spectral refinement, not metric stretching. The constants carry the signature. Session 41 tests this.
**Results file**: `sessions/session-41/session-41-results-workingpaper.md`

---

## I. PI Directive: Spectral Refinement Cosmology

The S40 addenda established:
- Particles are sequential excitations of a static phononic crystal substrate (Einstein Addendum 1)
- The substrate's standing waves are eigenmodes of D_K on Jensen-deformed SU(3) (Baptista Addendum)
- The fold is a resonance condition, not just a band edge (Tesla Addendum)
- S_B decomposes into CC (a_0), gravity (a_2), and gauge physics (a_4) — three moments of one spectral sum

The PI now proposes: **expansion is spectral refinement.** At small tau (near round SU(3)), the Dirac spectrum is maximally degenerate — fewer distinct eigenvalues, fewer distinct modes, larger effective "cells" in the phononic crystal. As tau increases, the Jensen deformation lifts degeneracies, eigenvalues split, the crystal gains resolution. Space was smaller not because stuff was packed tighter, but because there were fewer points of space.

This inverts standard BBN:
- **Standard**: universe starts hot/dense, cools, hydrogen forms when T drops below binding energy
- **Framework**: universe starts coarse, refines, hydrogen "just happens" when the phonon wavelength crosses the atomic scale

The session has three tracks:
1. **Straightforward gates from S40 handoff** (W1): off-Jensen BCS, alternative spectral functionals
2. **Spectral refinement computation** (W2): eigenvalue degeneracy count, mode resolution, effective expansion rate
3. **Conceptual exploration** (W3): agents contemplate the coarse-to-fine picture and its observable consequences

---

## II. Wave Structure

### Dependency Graph

```
WAVE 1 (S40 handoff gates — straightforward, pre-registered)
  W1-1: Off-Jensen BCS at g_73          [HESS-40 softest direction]
  W1-2: S_F through transit             [Dirac fermionic spectral action, NEW]
  W1-3: LOG-SIGNED-40                   [Paasch signed logarithmic sum, zero-cost]
  W1-4: M_KK from gauge coupling RGE    [e^{-2*0.190} = 0.684 vs SM g1/g2]
         |
         v
WAVE 2 (Spectral refinement — the new physics)
  W2-1: Degeneracy count N_eff(tau)     [count non-degenerate eigenvalues vs tau]
  W2-2: Mode resolution dN_eff/dtau     [rate of spectral refinement]
  W2-3: Effective H(tau)                [map refinement rate to expansion rate]
  W2-4: Hydrogen threshold tau_H        [tau where characteristic wavelength = a_0]
  W2-5: Constants at early tau          [alpha, G_N, gauge couplings from truncated spectral sums]
         |
         v
WAVE 3 (Conceptual exploration — directed agent contemplation)
  W3-1: CMB as substrate spectrum       [reinterpret CMB blackbody as crystal mode density]
  W3-2: BBN without hot                 [nucleosynthesis from spectral refinement]
  W3-3: LRD/JWST compatibility          ["already galaxies" from resolution threshold]
  W3-4: Constants as tau-snapshots      [do measured constants carry transit signature?]
```

---

## III. Wave 1: S40 Handoff Gates

### W1-1: Off-Jensen BCS at g_73

**Priority 1 from S40 handoff. 22/22 reviewers endorsed.**

Deform the metric at the fold by epsilon * delta_g_73 (the softest Hessian direction, H = 1572). Compute at 5 epsilon values in [0.001, 0.01, 0.05, 0.1, 0.5]:
- B2 gap Delta_B2(epsilon)
- [iK_7, D_K(epsilon)] commutator (does U(1)_7 survive?)
- Rank-1 fraction of V(B2,B2)(epsilon)
- QRPA stability (all omega^2 > 0?)
- M_max Thouless parameter

**Gate B2-OFFJ-41:**
- PASS: B2 gap and rank-1 within 20% of Jensen values at epsilon = 0.1
- FAIL: B2 gap closes or rank-1 drops below 50%

**Baptista note (S40 collab §3.1):** The g_73 deformation mixes U(1) with the C^2 complement — the same channel that determines sin^2(theta_W). If [iK_7, D_K] breaks at finite epsilon, the BCS selection rules change fundamentally.

**Cost**: Medium (5 Dirac spectrum computations at the fold + BCS for each)

### W1-2: Fermionic Spectral Action Through Transit

**New. Proposed by Dirac (S40 addendum §3-6). Never computed.**

Evaluate S_F(tau) = <J psi_BCS(tau), D_K(tau) psi_BCS(tau)> at 20 tau values in [0.10, 0.30].

S_F is linear in D (not quadratic), state-dependent (involves psi_BCS), and does NOT contain the cosmological constant (no a_0 term). The structural monotonicity theorem does not apply. If S_F has a minimum at or near the fold, the fermionic term provides the restoring force that S_B cannot.

**Gate SF-TRANSIT-41:**
- PASS: S_F has a local minimum or sign change in [0.15, 0.25]
- FAIL: S_F monotonic across full range

**Inputs**: Existing D_K eigenvalues + BCS ground state wavefunctions from S35-S40
**Cost**: Low (matrix elements from existing data)

### W1-3: Signed Logarithmic Sum (LOG-SIGNED-40)

**Paasch addendum correction. Zero-cost on existing data.**

Compute V_log^signed(tau) = +(1/2) sum_B d_n ln(lambda_n^2) - (1/2) sum_F d_n ln(lambda_n^2) at 20 tau values in [0.10, 0.30], using existing eigenvalue data from s37_cutoff_sa.npz with boson/fermion labels from BdG classification.

The unsigned logarithmic sum is monotonic (proven, covered by CUTOFF-SA-37). The SIGNED sum is NOT covered because the relative minus sign breaks the monotonicity argument. The concavity of ln amplifies gap-edge modes where F/B asymmetry is maximal (10-37%).

**Gate LOG-SIGNED-41:**
- PASS: Local minimum in [0.10, 0.25]
- FAIL: Monotonic across full range

**Cost**: Seconds (re-sum existing eigenvalues)

### W1-4: M_KK from Gauge Coupling RGE

**18/22 S40 reviewers flagged as the bottleneck for external predictions.**

The framework gives g_1/g_2 = e^{-2*0.190} = 0.684 at the fold. The SM value at M_Z is g'/g = tan(theta_W) = 0.553. RG-evolve the SM couplings from M_Z upward and find the scale where g_1/g_2 = 0.684. That scale is M_KK.

Account for:
- Dynkin index normalization (sqrt(3/5) for hypercharge)
- Two-loop RGE coefficients
- Threshold corrections from KK tower

**Output**: M_KK in GeV. This converts every result from M_KK units to physical units.
**Cost**: Low (analytic RGE integration)

---

## IV. Wave 2: Spectral Refinement

### W2-1: Degeneracy Count N_eff(tau)

The central new computation. At each tau in [0.00, 0.50] at 50 points:
- Compute the full Dirac eigenvalue spectrum at max_pq_sum = 6
- Count the number of DISTINCT eigenvalues (within tolerance 10^{-6}) — call this N_eff(tau)
- Count the number of non-degenerate modes (multiplicity = 1) — call this N_split(tau)
- Record the average degeneracy d_avg(tau) = N_total / N_eff(tau)

At tau = 0 (round SU(3), maximal symmetry): eigenvalues within each (p,q) sector are highly degenerate. N_eff is small, d_avg is large.
At tau = 0.190 (fold): degeneracies lifted by Jensen deformation. N_eff is larger, d_avg is smaller.
At tau = 0.50: further splitting. N_eff larger still.

N_eff(tau) IS the spectral resolution of the phononic crystal. Its growth rate is the framework's expansion.

**Output**: N_eff(tau), N_split(tau), d_avg(tau) as arrays. Plot.
**Cost**: Medium (50 spectrum computations — most already cached from prior sessions)

### W2-2: Mode Resolution Rate dN_eff/dtau

From W2-1 output:
- Compute dN_eff/dtau by finite differences
- Identify any tau where dN_eff/dtau has a maximum (rapid refinement epoch)
- Compare the refinement rate at the fold to the refinement rate at tau = 0

If dN_eff/dtau peaks near the fold, the framework predicts a burst of "space creation" coincident with the BCS transit — particle creation and space creation are the same event.

**Output**: dN_eff/dtau(tau) array. Location and magnitude of peak.

### W2-3: Effective Expansion Rate H_eff(tau)

Map the spectral refinement to an effective Hubble parameter:

    H_eff(tau) = (1/N_eff) * dN_eff/dtau * |dtau/dt|

where dtau/dt is the transit speed from the modulus equation of motion (TAU-DYN-36: v_terminal = 26.5 at the fold).

Compare H_eff at the fold to H_BBN ~ 1 s^{-1} (standard BBN expansion rate at T ~ 1 MeV). This requires M_KK from W1-4 to convert to physical units.

**Output**: H_eff(tau) in s^{-1} (once M_KK is known). Comparison to H_BBN.

### W2-4: Hydrogen Threshold tau_H

Find the tau where the characteristic phonon wavelength equals the Bohr radius:

    lambda_char(tau) = 1 / lambda_min(tau)

where lambda_min is the lowest non-trivial eigenvalue of D_K at that tau. When lambda_char(tau) = a_0 = 0.529 Angstrom = 0.529 * 10^{-10} m:

    lambda_min(tau_H) = 1/a_0 = 1.89 * 10^{10} m^{-1}

In M_KK units: lambda_min(tau_H) = a_0^{-1} / M_KK. This requires M_KK from W1-4.

Alternative (M_KK-independent): find the tau where the RATIO of the lowest eigenvalue to the fold eigenvalue matches the RATIO of the Bohr radius to the KK scale. This is a dimensionless comparison.

**Output**: tau_H (hydrogen resolution threshold). Map to cosmic time via tau(t) trajectory.

### W2-5: Constants at Early tau

Compute the Seeley-DeWitt coefficients a_0(tau), a_2(tau), a_4(tau) at 10 tau values in [0.00, 0.50]:
- a_0 = (1/2) sum_n d_n |lambda_n|^0 = total mode count (weighted)
- a_2 propto sum_n d_n |lambda_n|^{-2} (gravity)
- a_4 propto sum_n d_n |lambda_n|^{-4} (gauge couplings)

The RATIOS a_2/a_0 and a_4/a_2 determine:
- Newton's constant (in M_KK units)
- The fine structure constant
- The gauge couplings

Track these ratios as functions of tau. If they change significantly between tau = 0 and tau = 0.190, the "constants" are not constant through the transit — they evolved as the crystal refined. The values we measure today are snapshots of the spectral sum at the current tau.

**Output**: a_0(tau), a_2(tau), a_4(tau), alpha(tau), G_N(tau) as arrays. Plot.
**Cost**: Low (existing eigenvalue data)

---

## V. Wave 3: Conceptual Exploration

These are agent-directed contemplation tasks. Each agent receives the W1-W2 results and a specific question. Output is a collab addendum, not a gate verdict.

### W3-1: CMB as Substrate Spectrum (Tesla + Quantum Acoustics)

**Question**: If the CMB is not thermal radiation from a plasma wall but the substrate's standing-wave spectrum at the epoch when the crystal first supported EM-scale patterns, what does it predict?

Key inputs:
- Weyl's law: eigenvalue density on a compact d-manifold approaches N(lambda) ~ C_d * vol * lambda^d
- A phononic crystal with mode density following Weyl's law produces a Planck-like spectrum
- The "temperature" is set by the eigenvalue spacing, not by thermal equilibrium

**Deliverable**: Does Weyl's law on SU(3) at the appropriate tau reproduce 2.725 K? What are the deviations from a perfect blackbody, and do they match the CMB spectral distortion bounds (COBE/FIRAS: |Delta I/I| < 10^{-5})?

### W3-2: BBN Without Hot (Einstein + Nazarewicz + Landau)

**Question**: If nucleosynthesis proceeds by spectral refinement (the crystal becoming fine enough to support nuclear-scale patterns) rather than thermal cooling, what happens to the primordial abundances?

Key inputs:
- D/H = 2.527 +/- 0.030 x 10^{-5} (observed)
- He-4 mass fraction Y_P = 0.2449 +/- 0.0040 (observed)
- Li-7/H = 1.6 +/- 0.3 x 10^{-10} (observed, 3x below BBN prediction)
- The transit profile tau(t) is non-uniform — it accelerates through the fold

**Deliverable**: Qualitative assessment of whether spectral refinement can reproduce the observed abundances. Does the lithium problem resolve if the expansion rate during the Li-7 window differs from standard BBN? What are the specific tau-thresholds for deuterium, helium, and lithium patterns?

### W3-3: JWST / LRD Compatibility (Little Red Dots + Cosmic Web)

**Question**: JWST finds "already galaxies" at z > 10. In the framework, these didn't form — the substrate at that epoch had already refined past the galaxy-support threshold. What does this predict?

Key inputs:
- LRD number densities at z ~ 5-7 (Session 40 LRD collab)
- The spectral resolution N_eff(tau) from W2-1
- The tau-to-redshift mapping from tau(t) trajectory

**Deliverable**: At what tau does the crystal support galaxy-scale structure? Does the framework predict a sharp resolution threshold or a gradual emergence? How does this compare to the observed LRD number density evolution?

### W3-4: Constants as Transit Snapshots (Connes + Spectral Geometer + Feynman)

**Question**: The constants we measure today are spectral sums evaluated at the current tau. If the crystal was coarser at early tau, the sums had fewer terms. Do the constants carry a detectable signature of having evolved through the transit?

Key inputs:
- W2-5 output: a_0(tau), a_2(tau), a_4(tau)
- The clock constraint dalpha/alpha = -3.08 tau_dot (S22d)
- CMB constraints on Dalpha/alpha < 10^{-2} at z ~ 1100
- Quasar absorption constraints on Dalpha/alpha < 10^{-5} at z ~ 2-4

**Deliverable**: Are the framework's predicted constant variations consistent with observational bounds? Is there a tau_freeze beyond which the constants are effectively static (the crystal is fully refined)? What is the spectral signature of "incomplete refinement" — a truncated sum vs a full sum?

---

## VI. Pre-Registered Master Gates

| Gate | Criterion | Priority |
|:-----|:----------|:---------|
| B2-OFFJ-41 | B2 gap within 20% at epsilon = 0.1 | 1 |
| SF-TRANSIT-41 | S_F non-monotonic in [0.15, 0.25] | 2 |
| LOG-SIGNED-41 | V_log^signed non-monotonic | 3 |
| N-EFF-41 | N_eff(0.190) / N_eff(0) > 1.5 | 4 |
| TAU-H-41 | tau_H exists in [0, 0.5] at M_KK from W1-4 | 5 |

---

## VII. What NOT to Do

1. **Do not search for new equilibrium stabilization mechanisms.** The constraint surface is mapped across all 28 dimensions. The search is complete (HESS-40, 22/22 positive, margin 10^7).

2. **Do not re-gate closed results.** The 27 closures are permanent. The S40 master collab confirmed 22/22 reviewers unanimous.

3. **Do not treat the spectral refinement picture as proven.** W2 computations will determine whether N_eff(tau) actually increases, whether it increases enough, and whether the rate matches cosmological expansion. The picture is a hypothesis to be tested, not a result to be confirmed.

4. **Do not conflate resolution with temperature.** The spectral refinement picture replaces thermal cooling with crystal refinement. These make different predictions. Keep them separate. If they converge (Weyl's law → Planck spectrum), that convergence is a result, not an assumption.

---

## VIII. Session Logistics

**Agent allocation:**
- W1-1 through W1-4: gen-physicist (parallel single-agent computations)
- W2-1 through W2-5: gen-physicist (sequential, W2-2 depends on W2-1, etc.)
- W3-1: Tesla + Quantum Acoustics (2-agent workshop, skeleton document)
- W3-2: Einstein + Nazarewicz + Landau (3-agent workshop)
- W3-3: Little Red Dots + Cosmic Web (2-agent workshop)
- W3-4: Connes + Spectral Geometer + Feynman (3-agent workshop)

**Wave timing:**
- W1: First (parallel, 4 computations)
- W2: After W1-4 completes (needs M_KK for physical units in W2-3, W2-4)
- W3: After W2 completes (needs N_eff(tau) and constants-vs-tau data)

**Output discipline:** One writer per output file. Workshop outputs use the S38 skeleton pattern (pre-labeled sections per agent per round).
