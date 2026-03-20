# Session 22a: Zero-Cost Calculation Bonanza — Tier 0 Sweep

## Session Type: COMPUTATION (zero-cost, existing data only)
## Agents: schwarzschild-penrose-geometer + quantum-acoustics-theorist + coordinator
## Session Goal: Execute ALL remaining zero-cost and near-zero-cost computations that can be run from existing data without eigenvector extraction. Produce numerical results with pre-registered pass/fail verdicts for every computation. Feed all results to Session 22b synthesis and Session 22c non-perturbative planning.

---

# 0. OPERATIONAL RULES — READ BEFORE ANYTHING ELSE

## TWO-PHASE STRUCTURE

**Phase A**: Independent computations (each agent runs assigned scripts in parallel).
**Phase B**: Cross-pollination and synthesis. Agents share results, find connections, report to coordinator. The document is NOT done when Phase A scripts finish.

**COMPLETION SIGNAL**: Session ends ONLY when coordinator sends: "SESSION 22a COMPLETE — all agents confirm." Coordinator polls each agent individually before sending this signal.

## MESSAGE PROTOCOL

**Work step, then inbox, work step, then inbox.** Never read more than 2 files or complete more than 1 computation block without checking messages. If you discover a connection to the other agent's domain, message IMMEDIATELY.

## COMPUTATION DISCIPLINE

Every result must be classified against its pre-registered Constraint Gate BEFORE any interpretation is attempted. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s22a_`

---

# I. CONTEXT: WHERE WE ARE

## The delta_T Result (The First Genuinely Negative Computational Result)

Session 21c (Phase 0) computed delta_T(tau) = T(tau) - tau using block-diagonal eigenvalues at 21 tau values. **Result: delta_T > 0 throughout [0, 2.0]**, decaying from 3399 at tau=0 to 3.04 at tau=2.0 with characteristic scale tau* = 0.28. No zero crossing. Not in any Z_3 sector. Not in any gauge-weighted decomposition.

The pre-registered gate: zero crossing in [0.15, 0.35] would upgrade to 55-62%; no crossing drops to approximately 35%. The gate fired. The block-diagonal self-consistency route is closed.

**Critical caveat (15/15 reviewers)**: The computation used block-diagonal eigenvalues with coupling/gap ratio of 4-5x at the gap edge. The coupled diagonalization (Session 22b, P1-2) remains untested. This is not accommodation — it is a statement about the known approximation error.

## Framework Status Entering Session 22

- **Probability**: 39-40% (R2 collab median), range 28-43%
- **Perturbative spectral routes**: ALL CLOSED (structural theorem, Dual Algebraic Trap)
- **Block-diagonal self-consistency**: CLOSED (delta_T > 0)
- **Surviving routes**: (1) Coupled diagonalization (P1-2), (2) BCS/Pomeranchuk channel, (3) Freund-Rubin flux (beta/alpha uncomputed), (4) Non-perturbative instantons, (5) Hubble friction without a minimum
- **New mechanism from R2 (SP)**: Slow-roll epsilon(tau) — Hubble friction may arrest the modulus without a potential minimum at all. This is now the highest-priority zero-cost computation.

## The Physical Window

Three Berry curvature monopoles:
- M0 at tau=0: (0,0)/(1,1) exact degeneracy, first-order coupling
- M1 at tau~0.10-0.15: (0,0) takes over gap edge from (1,0)/(0,1)
- M2 at tau~1.58: (0,0) surrenders gap edge back

Physical window [0.15, 1.55] where (0,0) singlet dominates gap edge. All known physical features cluster here: phi_paasch (0.15), BCS bifurcation (0.20), FR minimum (0.30), FR degenerate (0.375).

---

# II. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 21c Phase 0 synthesis**: `sessions/session-21/session-21c-phase0-synthesis.md`
   — Full Phase 0 results, structural theorems, three-monopole topology. Read completely.

2. **R2 master collab**: `sessions/session-21/session-21c-r2-master-collab.md`
   — Post-delta_T probability assessments. Sections VIII (Tier 0 priority table), IX (probability), X (conditional structure). THIS is the primary tasking document.

3. **Session 21b Valar plan**: `sessions/session-plan/session-21b-valar-plan.md`
   — Constraint Gate registry (Section VI). Pre-registered gates for every computation.

4. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:------------------|
| schwarzschild-penrose | R2 SP collab review (Section XI: `session-21c-r2-sp-collab.md`) — SP's elevation of slow-roll epsilon |
| quantum-acoustics | R2 QA collab review (Section XI: `session-21c-r2-quantum-acoustics-collab.md`) — Fano parameter, impedance mismatch, Jahn-Teller reinterpretation |

---

# III. PHASE A: COMPUTATION ASSIGNMENTS

## Agent Allocation

| Agent | Computations |
|:------|:------------|
| schwarzschild-penrose-geometer | SP-1: slow-roll epsilon(tau), SP-2: Weyl curvature at monopoles, SP-3: Euclidean action I_E at monopoles |
| quantum-acoustics-theorist | QA-1: acoustic impedance Z(tau), QA-2: Fano parameter q(tau), QA-3: delta_T decay profile fit |
| phonon-exflation-sim (if available) | Support: data loading, script validation, heavier numerics |
| coordinator | Tracks progress, routes cross-domain connections, assembles Phase B synthesis |

**NOTE**: phonon-exflation-sim is not assigned as a primary agent this session (it is reserved for Session 22b's eigenvector extraction). SP-geometer and QA-theorist should write and execute their own scripts using the existing .npz data.

---

### Computation SP-1: Slow-Roll Parameters epsilon(tau) and eta(tau)

**Primary**: schwarzschild-penrose-geometer
**Priority**: HIGHEST (elevated by SP in R2, now #1 after delta_T result)
**Runtime**: Minutes from existing data

**Background**: With no self-consistency fixed point and no perturbative potential minimum, SP identified Hubble friction as the only remaining perturbative stabilization mechanism. The modulus need not have a potential minimum — if epsilon < 1 throughout the physically relevant range [0.15, 0.55], Hubble friction arrests the modulus without a minimum. This reframes the question from "where does dV/dtau = 0?" to "is the potential flat enough that Hubble damping prevents runaway?"

**Equations**:

The slow-roll parameters for modulus tau with kinetic metric G_ττ = 5 (from Baptista Paper 15 eq 3.79):

```
epsilon(tau) = (1 / (2 G_ττ)) * (V'(tau) / V(tau))^2 = (1/10) * (V'(tau) / V(tau))^2

eta(tau) = (1 / G_ττ) * V''(tau) / V(tau) = (1/5) * V''(tau) / V(tau)
```

where V(tau) is the total perturbative potential from Session 20b data.

**Data source**: `tier0-computation/l20_vtotal_minimum.npz`
- Keys include V_total(tau), V_CW(tau), E_Casimir(tau) at 21 tau values
- Derivatives via finite differences (use 3-point central difference where possible)

**Protocol**:
1. Load `l20_vtotal_minimum.npz`. Extract V_total and its gradient dV/dtau.
2. Compute epsilon(tau) = (1/10) * (V'/V)^2 at each tau.
3. Compute eta(tau) = (1/5) * V''/V at each tau.
4. Also compute the Hubble parameter proxy H^2 ~ V(tau)/(3 M_Pl^2). The actual Hubble number requires M_scale which is a free parameter — compute epsilon and eta as dimensionless ratios independent of M_scale.
5. Plot epsilon(tau) and eta(tau) vs tau. Mark the physical window [0.15, 0.55] and the monopole locations M1 (~0.15) and FR minimum (~0.30).
6. **Key question**: Is epsilon < 1 anywhere in [0.15, 0.55]? Is it < 0.01 (strong slow-roll)?

**Pre-registered Constraint Gates** (SP, R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | epsilon < 0.01 throughout [0.15, 0.55] (ultra-slow roll) | 20 | +12-15 pp |
| COMPELLING | epsilon < 1 throughout [0.15, 0.55] (slow-roll satisfied) | 8 | +6-10 pp |
| INTERESTING | epsilon < 1 somewhere in [0.15, 0.55] but not throughout | 3 | +2-4 pp |
| NEUTRAL | epsilon > 1 throughout (no slow-roll) but eta < 0 (concave potential) | 1 | 0 pp |
| CLOSED | epsilon > 1 AND eta > 0 everywhere (no slow-roll, convex potential) | 0.3 | -4-6 pp |

**Note on V'''(0) = -7.2**: The cubic term means V' is not uniformly positive. Near tau=0, V' < 0 (potential initially curves down). Epsilon diverges as V -> 0. Compute from tau = 0.05 upward, avoid the tau=0 pole.

**Output**: `tier0-computation/s22a_slow_roll.py`, `tier0-computation/s22a_slow_roll.npz`, `tier0-computation/s22a_slow_roll.png`

---

### Computation SP-2: Weyl Curvature |C|^2 at Monopole Locations

**Primary**: schwarzschild-penrose-geometer
**Priority**: Medium
**Runtime**: Minutes from existing Riemann data

**Background**: SP proposed checking whether |C|^2 (Weyl curvature squared, the traceless part of the Riemann tensor) is minimized at the monopole locations. The Weyl hypothesis (Penrose) states physical solutions minimize complexity = |C|^2. If |C|^2 is minimized at M0 (tau=0) or M1 (tau~0.10-0.15), this provides a geometric selection principle for those tau values independent of V_eff.

**Equations**:

Weyl tensor in d dimensions: C_{abcd} = R_{abcd} - (1/(d-2))[g_{ac}R_{bd} - g_{ad}R_{bc} + g_{bd}R_{ac} - g_{bc}R_{ad}] + (1/((d-1)(d-2)))R[g_{ac}g_{bd} - g_{ad}g_{bc}]

On SU(3) (d=8), |C|^2 = C_{abcd}C^{abcd}

From Session 20a data: |Riem|^2, |Ric|^2, R_K are all precomputed.

**Data source**: `tier0-computation/r20a_riemann_tensor.npz`
- This contains the full Riemann tensor components R_{abcd}(tau) at 21 tau values

**Protocol**:
1. Load `r20a_riemann_tensor.npz`.
2. Compute the Weyl tensor C_{abcd} at each tau from R_{abcd}, R_{ab}, R.
3. Compute |C|^2(tau) = C_{abcd}C^{abcd}.
4. Plot |C|^2(tau) vs tau. Mark monopole locations M0 (0), M1 (~0.15), M2 (~1.58).
5. Does |C|^2 have a minimum? Where?
6. **Cross-check**: |Riem|^2 = |C|^2 + (4/(d-2))|Ric|^2 - (2/((d-1)(d-2)))R^2 (should verify this Bianchi decomposition).

**Pre-registered Constraint Gates** (SP proposal, R2 collab Table V.10):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| INTERESTING | |C|^2 minimized at tau in [0.15, 0.40] (Weyl selects physical window) | 4 | +2-4 pp |
| CLOSED | |C|^2 monotonically increasing (Weyl hypothesis irrelevant / selects tau=0) | 0.7 | -1 pp |
| PASS | |C|^2 minimized at tau=0 (confirms round metric is Weyl-optimal) | 1 | 0 pp |

**Output**: `tier0-computation/s22a_weyl_curvature.py`, `tier0-computation/s22a_weyl_curvature.npz`, `tier0-computation/s22a_weyl_curvature.png`

---

### Computation SP-3: Euclidean Action I_E at Three Monopoles

**Primary**: schwarzschild-penrose-geometer
**Priority**: High (Hawking's top priority, R2 collab)
**Runtime**: Lookup from existing curvature data (~30 minutes to code)

**Background**: Hawking (R2 collab) elevated the Euclidean path integral as an alternative selection mechanism that requires NO potential minimum. The path integral sums over ALL saddle points. The Euclidean action for each saddle is I_E = -S_E = -(1/16piG) integral R_K dvol (on a compact space with no boundary). If I_E(M1) > I_E(M0), the path integral exponentially suppresses M0 relative to M1, selecting the deformed metric without requiring a potential minimum.

**Equations**:

I_E(tau) = -(1/(16 pi G)) integral R_K(tau) dvol(tau)

On volume-preserving Jensen deformation: Vol(K) = constant, dvol = Vol(K). So:

I_E(tau) ~ -R_K(tau) * Vol(K) / (16 pi G)

The tau-independent factors cancel in the RATIO I_E(M0)/I_E(M1). Compute the ratio.

From Session 17b: R_K(tau) is an exact analytic function (stored in `sp2_final_verification.py` and `r20a_riemann_tensor.npz`).

**Protocol**:
1. Load R_K(tau) from existing curvature data (or re-derive from `sp2_final_verification.py`).
2. Evaluate R_K at M0 (tau=0), M1 (tau~0.15, use the exact crossing point from Session 21c neutrino data), M2 (tau~1.58).
3. Compute I_E(tau) ~ -R_K(tau) [the Vol and G factors cancel in ratios].
4. Compute the ratios: I_E(M1)/I_E(M0), I_E(M2)/I_E(M1).
5. The Euclidean path integral weight: exp(-I_E) = exp(R_K/16piG). Higher R_K = lower I_E = exponentially preferred.
6. **Key question**: Is R_K(M1) > R_K(M0)? If yes, M1 is Euclidean-preferred over M0.

**Pre-registered Constraint Gates** (Hawking R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| INTERESTING | I_E(M1) < I_E(M0) (M1 Euclidean-preferred) | 3 | +2-3 pp |
| COMPELLING | I_E ratio exp(-delta I_E) > 10 (exponential dominance of M1) | 8 | +5-8 pp |
| NEUTRAL | I_E(M1) > I_E(M0) (M0 preferred, but selection still occurs) | 1 | 0 pp |
| CLOSED | I_E identical at all three monopoles (no saddle preference) | 0.4 | -2 pp |

**Note**: R_K on SU(3) with Jensen deformation is given analytically by:
R_K(tau) = (1/4) * [n_1 * e^{-4tau} + n_2 + n_3 * e^{6tau}] (schematically from structure constants)
The exact formula is in `sp2_final_verification.py`. Load or recompute.

**Output**: `tier0-computation/s22a_euclidean_action.py`, `tier0-computation/s22a_euclidean_action.txt`

---

### Computation QA-1: Acoustic Impedance Z(tau) and Reflection Coefficient R_reflect(tau)

**Primary**: quantum-acoustics-theorist
**Priority**: High (QA + Tesla R2 proposal — new stabilization mechanism bypassing V_eff)
**Runtime**: Minutes from existing eigenvalue data

**Background**: QA (R2 collab, Section VI.2) identified that the acoustic impedance mismatch at the monopole boundaries M1 and M2 may dynamically confine the modulus via reflection, even without a potential minimum. The impedance Z(tau) ~ sqrt(rho * kappa) where rho is the phonon "mass density" (eigenvalue density) and kappa is the "bulk modulus" (eigenvalue gradient). A rolling modulus approaching M1 from tau > 0.15 encounters an impedance mismatch and may reflect.

**Physical interpretation**: This is a Fabry-Perot cavity in modulus space. M1 and M2 are partially reflecting boundaries. The modulus can be dynamically trapped between them without any potential minimum, purely through reflection losses at each boundary traversal.

**Equations**:

Define the phonon acoustic impedance from the Dirac spectrum:

```
rho(tau) = dN/domega |_{omega = gap(tau)}  [DOS at the gap edge]
kappa(tau) = d(gap)/dtau  [gap stiffness]
Z(tau) = sqrt(|rho(tau) * kappa(tau)|)
```

Reflection coefficient at a discontinuity in Z:
```
R_reflect = ((Z_2 - Z_1) / (Z_2 + Z_1))^2
```

At M1 (transition from pre-condensate to condensate-active window):
- Z_outside: DOS ~ 24 (fundamental multiplicity), gap softening
- Z_inside: DOS ~ 2 (singlet multiplicity), gap stabilizing

**Data sources**:
- `tier0-computation/s19a_sweep_data.npz` — Dirac eigenvalues by sector at 21 tau values
- `tier0-computation/kk1_bosonic_spectrum.npz` — bosonic modes at 4 tau values
- `tier0-computation/s21c_V_IR.npz` — V_IR data (gap behavior)

**Protocol**:
1. For each tau in the sweep: compute the fermionic gap edge = smallest fermionic eigenvalue.
2. Compute rho(tau) = multiplicity of gap-edge modes / (gap width epsilon) where epsilon = gap - next mode.
3. Compute kappa(tau) = d(gap)/dtau (numerical derivative).
4. Compute Z(tau) = sqrt(|rho * kappa|).
5. At M1 (tau~0.15): compute Z(tau_before) vs Z(tau_after). Compute R_reflect.
6. At M2 (tau~1.58): same.
7. **Key question**: Is R_reflect at M1 large enough (> 0.1, meaning > 10% reflection) to confine a rolling modulus?

**Pre-registered Constraint Gates** (QA R2 proposal):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | R_reflect > 0.30 at both M1 and M2 (cavity with >30% reflectivity) | 15 | +8-12 pp |
| COMPELLING | R_reflect > 0.10 at M1 (partial trapping) | 6 | +4-6 pp |
| INTERESTING | Impedance discontinuity confirmed (Z changes by factor >2 at M1) | 3 | +1-3 pp |
| CLOSED | Z(tau) smooth, no discontinuity at monopoles (R_reflect < 0.01) | 0.3 | -3-5 pp |

**Output**: `tier0-computation/s22a_impedance.py`, `tier0-computation/s22a_impedance.npz`, `tier0-computation/s22a_impedance.png`

---

### Computation QA-2: Fano Parameter q(tau) at Monopole Locations

**Primary**: quantum-acoustics-theorist
**Priority**: Medium (independent coupling strength measurement)
**Runtime**: Minutes from existing eigenvalue data

**Background**: QA (R2 collab, Novel Proposal #19) proposed computing the Fano resonance parameter q(tau) at the monopole locations. In scattering theory, the Fano parameter characterizes the interference between a discrete resonance and a continuum background. At a Berry curvature monopole, the gap-edge mode (discrete) mixes with continuum modes (the bulk spectrum) through the Kosmann-Lichnerowicz coupling. The Fano lineshape of the avoided crossing encodes the coupling strength — an independent measurement of the off-diagonal coupling without requiring eigenvector extraction.

**The Fano profile** near a resonance energy omega_0:

sigma(omega) ~ |omega - omega_0 + q*Gamma/2|^2 / |omega - omega_0 + i*Gamma/2|^2

where q is the Fano parameter (q=0: pure Lorentzian; q->infinity: symmetric Fano) and Gamma is the resonance width.

**At the monopoles**: The "resonance" is the gap-edge mode approaching the avoided crossing. The "continuum" is the bulk spectral density. The lineshape of the gap-edge eigenvalue trajectory encodes q.

**Data sources**:
- `tier0-computation/s21c_neutrino_fine_grid.npz` — fine-grid R(tau) data near M2 (tau~1.58)
- `tier0-computation/s19a_sweep_data.npz` — coarse-grid eigenvalues for M1

**Protocol**:
1. Near M2 (tau~1.58): extract eigenvalue trajectories of the 3 lightest eigenmodes.
2. Fit the gap-edge eigenvalue trajectory near tau_M2 to a Fano profile in tau-space.
3. Extract q from the fit asymmetry.
4. Near M1 (tau~0.11-0.15): similarly from coarse-grid data (will be less precise).
5. **Connection to off-diagonal coupling**: Fano q relates to the matrix element ratio |V|^2 / (Delta_epsilon * Gamma). If |q| is large, the coupling is strong relative to the level spacing — consistent with the 4-5x coupling/gap ratio from Session 21b.

**Pre-registered Constraint Gates** (QA proposal):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| COMPELLING | |q| > 2 at M2 (strong coupling, Fano-dominated lineshape) | 5 | +2-4 pp |
| INTERESTING | |q| in [1, 2] (mixed Lorentzian/Fano) | 3 | +1-2 pp |
| NEUTRAL | |q| < 1 (Lorentzian-dominated) | 1 | 0 pp |

This is a consistency check on the coupling estimate, not a primary gate.

**Output**: `tier0-computation/s22a_fano.py`, `tier0-computation/s22a_fano.txt`

---

### Computation QA-3: delta_T Decay Profile Fitting

**Primary**: quantum-acoustics-theorist
**Priority**: Medium (structural understanding of the result)
**Runtime**: Minutes from existing data

**Background**: The delta_T(tau) result shows exponential decay from 3399 to 3.04 across [0, 2.0]. Tesla (R2 collab) proposed that the characteristic scale tau* = 1/gamma ~ 0.28 is suggestively close to the FR minimum at tau = 0.30, and further proposed a Bragg bandgap interpretation where the e^{-4tau} modulation period creates a bandgap in tau-space. This computation characterizes the decay profile and tests whether the decay rate is algebraically determined by the Dynkin indices.

**Data source**: `tier0-computation/s21c_cp1_investigation.npz`
- Keys include: `delta_T_total`, `delta_T_b1`, `delta_T_b2`, `delta_T_z3_0`, `delta_T_z3_1`, `delta_T_z3_2`, `tau_values`

**Protocol**:
1. Load delta_T_total from `s21c_cp1_investigation.npz`.
2. Fit to exponential: delta_T(tau) = A * exp(-gamma * tau). Extract A and gamma.
3. Fit to double exponential: delta_T = A1 * exp(-g1*tau) + A2 * exp(-g2*tau). Better fit?
4. Compute the half-wavelength of the e^{-4tau} modulation: pi/(2) ~ 1.57. Compare to physical window width [0.15, 1.55] = 1.40. Agreement within 11% (Tesla's Bragg hypothesis)?
5. **Test the algebraic determination**: The Dynkin embedding index gives b1/b2 = 4/9. Does the decay rate gamma relate algebraically to 4 (from e^{-4tau})? Specifically: gamma_fit vs 4 (exact from flux channel)?
6. **Sign structure analysis**: delta_T_b1 and delta_T_b2 are individually negative (driven by gauge-weighted sum). delta_T_total is positive (singlet sector dominates). Compute the singlet contribution = delta_T_total - delta_T_b1 * weight - delta_T_b2 * weight. This isolates the (0,0) singlet's role.

**Output**: `tier0-computation/s22a_delta_T_profile.py`, `tier0-computation/s22a_delta_T_profile.txt`, `tier0-computation/s22a_delta_T_profile.png`

---

### Computation QA-4: phi_paasch Ratio Curve at All 21 tau Values

**Primary**: quantum-acoustics-theorist (using existing eigenvalue data)
**Priority**: Medium (Paasch pre-registered test)
**Runtime**: Minutes

**Background**: Session 12 found m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15, which is 0.0005% from phi_paasch = 1.53158 (= solution to x = e^{-x^2}). This result was found at a single tau value. Paasch (R2 collab) pre-registered: compute this ratio at ALL 21 tau values and check whether the phi_paasch match is specific to tau~0.15, or whether the ratio tracks phi_paasch along a curve.

**Data source**: `tier0-computation/s19a_sweep_data.npz`
- Dirac eigenvalues by sector (p,q) at 21 tau values

**Protocol**:
1. For each tau: extract the lowest eigenvalue in the (3,0) sector and the lowest in the (0,0) sector.
2. Compute ratio r(tau) = lambda_{(3,0),min}(tau) / lambda_{(0,0),min}(tau).
3. Mark phi_paasch = 1.53158 on the plot.
4. Does r(tau) cross phi_paasch? At what tau? Is tau_phi consistent with M1 (~0.15)?
5. **Pre-registered test (Paasch)**: r(tau_phi) = phi_paasch to better than 0.01% and tau_phi in [0.13, 0.17] => COMPELLING evidence for Paasch mass quantization at the monopole.

**Pre-registered Constraint Gates** (Paasch R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | r(tau) crosses phi_paasch at tau_phi in [0.14, 0.16] and dip below 0.01% | 20 | +6-10 pp |
| COMPELLING | r(tau) tracks phi_paasch within 0.1% for tau in [0.10, 0.20] | 8 | +4-6 pp |
| INTERESTING | r(tau) crosses phi_paasch at some tau | 3 | +1-2 pp |
| CLOSED | r(tau) never within 1% of phi_paasch at any tau | 0.3 | -3-5 pp |

**Output**: `tier0-computation/s22a_paasch_curve.py`, `tier0-computation/s22a_paasch_curve.npz`, `tier0-computation/s22a_paasch_curve.png`

---

### Computation QA-5: Sound Speed Ratio c_{u1}/c_{su2} at tau = 0.30

**Primary**: quantum-acoustics-theorist
**Priority**: Low-medium (Tesla R2 proposal — Weinberg angle as phonon anisotropy)
**Runtime**: Minutes

**Background**: Tesla (R2 collab) proposed that the Weinberg angle sin^2(theta_W) = 0.231 is the square of the sound speed RATIO between U(1) and SU(2) phonon branches:

sin^2(theta_W) = c_{u1}^2 / (c_{u1}^2 + c_{su2}^2)

The sound speed in each sector is c_s = d(omega)/dk|_{k->0} ~ sqrt(dE/dn)|_n. For the Dirac spectrum sectors:
- U(1) branch: lowest eigenvalues in sectors with (p,q) -> Y dominance (p < q sectors)
- SU(2) branch: lowest eigenvalues in sectors with I^2 dominance (p > q sectors)

At tau = 0.30 (the FR minimum / Weinberg angle point), this ratio should reproduce sin^2(theta_W) = 0.231.

**Data source**: `tier0-computation/s19a_sweep_data.npz` at tau=0.30 (index 3)

**Protocol**:
1. At tau = 0.30: extract eigenvalues from U(1)-dominated sectors (select using the b1 weighting from branching computation).
2. Extract eigenvalues from SU(2)-dominated sectors.
3. Compute the ratio of lowest eigenvalues: c_{u1}/c_{su2} = lambda_{u1,min}/lambda_{su2,min}.
4. Compute sin^2(theta_W)_predicted = c_{u1}^2/(c_{u1}^2 + c_{su2}^2).
5. Compare to experimental 0.231.

This is a consistency check, not a primary gate. Even a 10% agreement would be interesting given the coarseness of the sector classification.

**Output**: Append to `s22a_impedance.txt` (no separate file needed — a few lines suffices)

---

### Computation SP-4: Low-Mode Level Statistics (Brody Parameter q)

**Primary**: schwarzschild-penrose-geometer (using existing data; Berry was originally assigned this but is in Session 22c)
**Priority**: Medium (CP-2 test)
**Runtime**: Minutes

**Background**: The Session 21b result showed Poisson statistics across the bulk spectrum. Session 21c resolved the apparent contradiction: Poisson is measured intra-sector; Kosmann coupling acts inter-sector. A falsifiable prediction from Session 21c: the lowest 20-50 modes should show deviation from Poisson — Brody parameter q ~ 0.3-0.5 (intermediate statistics between Poisson and GOE), since the coupling/gap ratio is 4-5x only for the lowest modes.

**Data source**: `tier0-computation/s19a_sweep_data.npz`

**Protocol**:
1. Extract the 50 lowest Dirac eigenvalues ACROSS ALL SECTORS at tau = 0.30, 0.50, 1.00.
2. Unfold by the cumulative spectral density.
3. Compute nearest-neighbor spacing distribution P(s).
4. Fit the Brody distribution: P(s) = A * s^q * exp(-c * s^(q+1)) where q=0 is Poisson, q=1 is GOE.
5. Compare to bulk Brody parameter from Session 21b (q ~ 0 for bulk, Poisson).
6. **Pre-registered**: low-mode q > 0.3 at tau = 0.30 confirms CP-2 coupling prediction.

**Output**: Append to `s22a_slow_roll.py` or create `tier0-computation/s22a_level_stats.py`. Minimal output: one table of q values.

---

### Computation SP-5: DNP Stability Bound lambda_L/m^2(tau)

**Primary**: schwarzschild-penrose-geometer
**Priority**: Low-medium (KK pre-registration)
**Runtime**: Minutes from existing data

**Background**: KK (R2 collab) cited the Duff-Nilsson-Pope (KK Paper 11) stability bound: lambda_L >= 3m^2 for TT 2-tensors on (SU(3), g_Jensen). This is the Lichnerowicz bound — violation at some tau would signal a non-perturbative instability in the TT sector that could drive a transition. The ratio lambda_L_min(tau)/m^2_gauge(tau) should be checked.

**Data source**: `tier0-computation/l20_TT_spectrum.npz` — TT eigenvalues

**Protocol**:
1. Load the TT spectrum. Extract the minimum TT eigenvalue lambda_L_min(tau) at each tau.
2. The gauge mass squared from Session 17a: m^2_gauge(tau) = g_1^2(tau) * v^2 where g_1/g_2 = e^{-2tau}.
3. In natural units at the KK scale: m^2_gauge ~ e^{-4tau} (proportional to g_1^2).
4. Compute the ratio lambda_L_min(tau) / m^2_gauge(tau) ~ lambda_L_min(tau) * e^{4tau}.
5. Does this ratio drop below 3 at any tau? If yes: the DNP bound is violated and the TT sector is unstable.

**Output**: Append to `s22a_weyl_curvature.txt` (a few lines)

---

# IV. PHASE B: CROSS-POLLINATION SYNTHESIS

After Phase A computations complete, all agents switch to synthesis mode.

## Cross-Pollination Seed Questions

**SP -> QA**: "The slow-roll epsilon result — does it connect to the impedance Z(tau)? If epsilon is large (fast roll) but Z shows high reflectivity at M1, could reflection arrest what slow-roll cannot?"

**QA -> SP**: "The Fano parameter at M2 — does it tell us anything about the Euclidean saddle point weight at M2 (SP-3)? If the coupling is strong (large |q|), the monopole is spectrally active and should contribute to the path integral."

**Both -> coordinator**: "Do the slow-roll and impedance results, taken together, bound the DESI parameter w_0? The modulus kinetics determine w_eff. If the modulus is slow-roll and/or reflected, what equation-of-state does that produce?"

**Both -> coordinator**: "The phi_paasch crossing location tau_phi — is it coincident with M1, with the BCS bifurcation (tau=0.20), or with neither? Does it align with any of the other features in the physical window?"

## Required Synthesis Content

The designated writer (coordinator) must assemble:

1. **Phase A Results Table**: Each computation, result, Constraint Gate verdict, probability shift.
2. **Connection map**: Which results reinforce each other? Which contradict?
3. **Slow-roll synthesis**: Given epsilon(tau), which cosmological scenario is most likely? Does Hubble friction work as a stabilizer?
4. **Updated probability**: Per-agent assessment + panel consensus.
5. **Handoff notes for 22b**: What do the zero-cost results imply for the coupled diagonalization priority?
6. **Handoff notes for 22c**: What do these results imply for the BCS/Pomeranchuk channel scan?

---

# V. PRE-REGISTERED SCENARIOS

The R2 collab registered four conditional probability structures (Section X of R2). This session will constrain which scenario is active:

| Scenario | Trigger | Posterior |
|:---------|:--------|:----------|
| 1: Coupled delta_T crossing | (22b result) | 50-58% |
| 2: Coupled delta_T monotonic | (22b result) | 30-35% |
| 3: BCS attractive pairing | (22c result) | 48-55% |
| 4: beta/alpha = 0.28 from 12D | (future computation) | 52-70% |

**Session 22a constrains the starting probability for scenarios 1-4.**
- If epsilon < 1 (slow-roll): prior on scenario 1 rises (delta_T coupled crossing in slow-roll regime more likely)
- If epsilon > 1 + no impedance trapping: probability floor drops regardless of coupled computation

---

# VI. OUTPUT FILES

## Primary output (coordinator assembles after Phase B):

`sessions/session-22/session-22a-synthesis.md`

Must contain:
1. Phase A results table with Constraint Gate verdicts
2. Per-computation numerical results
3. Cross-pollination findings
4. Updated probability assessment (per-agent + panel)
5. Handoff notes for Sessions 22b and 22c

## Computation output files:

| File | Computation | Format |
|:-----|:-----------|:-------|
| `s22a_slow_roll.py/npz/png` | SP-1: epsilon, eta | All three |
| `s22a_weyl_curvature.py/npz/png` | SP-2: |C|^2 | All three |
| `s22a_euclidean_action.py/txt` | SP-3: I_E at monopoles | Script + text |
| `s22a_impedance.py/npz/png` | QA-1: Z(tau) | All three |
| `s22a_fano.py/txt` | QA-2: Fano q | Script + text |
| `s22a_delta_T_profile.py/txt/png` | QA-3: decay fit | All three |
| `s22a_paasch_curve.py/npz/png` | QA-4: phi_paasch curve | All three |
| `s22a_level_stats.py` | SP-4: Brody q | Script + inline output |

---

# VII. THE SAGAN STANDARD (Unchanged)

1. **Pre-registered**: Constraint Condition stated BEFORE computation. (Done above.)
2. **Falsifiable**: Numerical thresholds specified. (Done in Constraint Gate tables.)
3. **Non-accommodating**: Each mechanism was proposed before the delta_T result.
4. **Computable**: All scripts execute from existing .npz data in < 5 minutes each.
5. **Honest**: CLOSED means CLOSED. The delta_T result set the standard. Honor it.

---

# VIII. WHAT THIS SESSION IS REALLY ABOUT

The framework has just taken its first clean negative result. The panel responded appropriately — downward revision, not abandonment. Now the question is: what can be established at zero cost before the expensive coupled computation runs?

The slow-roll epsilon(tau) is the most important of these zero-cost checks. If epsilon < 1 in [0.15, 0.55], the modulus may not need a potential minimum at all — Hubble friction provides the arrest mechanism. This is not a rescue mechanism invented after the delta_T failure; SP proposed it during R1 (before the delta_T computation ran). It is a pre-registered alternative to the self-consistency route.

The impedance mismatch is the second most important. If Z(tau) shows a sharp discontinuity at M1 and M2, the physical window is dynamically active — a Fabry-Perot cavity in modulus space. This is a mechanism entirely orthogonal to the spectral sum closes and the self-consistency map. It operates on mode structure, not on energy extremization.

These are not desperation moves. They are the correct next steps given what is known.

---

*"The framework has not earned the right to be believed. It has earned the right to have its geometry computed. These computations are part of that geometry."*
*— Coordinator synthesis, Session 21c*
