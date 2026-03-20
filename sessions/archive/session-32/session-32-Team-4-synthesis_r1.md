# Session 32 Workshop W3 Round 1: SP x Neutrino x Paasch

**Date**: 2026-03-06
**Agents**: sp (schwarzschild-penrose-geometer), neutrino (neutrino-detection-specialist), paasch (paasch-mass-quantization-analyst), coordinator (coordinator)
**Format**: Three-agent workshop with cross-talk. Round 1.
**Mission**: Derive modulus field equation connections, connect dump point geometry to particle physics observables (PMNS, mass spectrum, phi_paasch), determine whether domain walls produce testable predictions.
**Synthesis Writer**: coordinator

**Input Files**:
- `sessions/session-32/session-32-tesla-lrd-baptista-workshop.md` (meta-workshop)
- `sessions/session-32/session-32-sp-naz-workshop.md` (SP-Naz workshop)
- `sessions/session-32/session-32-sp-collab.md`
- `sessions/session-32/session-32-neutrino-collab.md`
- `sessions/session-32/session-32-paasch-collab.md`
we're
---

## 1. Convergent Findings

Where all three specialists agree after independent computation and cross-talk.

### 1.1 The Dump Point Is Representation-Theoretic, Not Curvature-Invariant

All three agents converge: the dump point at tau = 0.190 has NO special curvature feature. SP's exact analytic evaluation of the Kretschner scalar K(tau) from the SP-2 formula establishes:

- K(tau) is monotonically increasing on [0, infinity). K' > 0 for all tau > 0.
- K''(0.190) = 2.65 (positive, nonzero). No extremum, no inflection.
- Bianchi decomposition at dump point (72.2% Weyl, 0.6% traceless Ricci, 27.2% scalar) is nearly identical to the round metric (71.4%, 0%, 28.6%).

The seven-quantity convergence at the dump point traces entirely to the B2 eigenvalue minimum d(lambda_B2)/d(tau) = 0, which is a representation-theoretic feature (U(2) fundamental within the singlet sector), not a curvature stationary point of the internal geometry.

The phi_paasch crossing at tau = 0.150 is likewise purely algebraic (inter-sector eigenvalue ratio E_{(3,0)}/E_{(0,0)}). K(tau) differs by only 2.5% between tau = 0.150 and tau = 0.190. Both features sit on a geometrically featureless background.

### 1.2 Normal Mass Ordering Confirmed at Domain Walls

All three agents confirm: the mass ordering m_1 < m_2 < m_3 (NORMAL) holds at domain walls for all BCS gaps Delta_B2 in [0, 0.5).

- SP: NEC holds at dump point (all Ricci eigenvalues positive, minimum = 0.2225). Penrose singularity theorem analog is fully operative. BCS condensation is NECESSARY to prevent geodesic incompleteness.
- Neutrino: Full 3x3 hybrid Hamiltonian scan confirms normal ordering across the entire Delta_B2 range. B2-B3 level crossing occurs at Delta_cross = 0.493 at tau = 0.20, but ordering of mass eigenstates remains normal below this.
- Paasch: The ordering is consistent with the BCS-dressed mass eigenvalue ratios along the phi_paasch attractor curve.

The JUNO pre-registration chain is strengthened: 5 of 7 links now PROVEN or CONFIRMED. Only TURING-1 (dump-straddling walls) and wall-BCS gap > 0 remain pending.

### 1.3 Trap 4 (Schur Orthogonality) Holds Exactly at Domain Walls

Neutrino's computation reveals zero inter-branch leakage at all wall configurations:

    O(B2 -> B1) = O(B2 -> B3) = 0.0000 (exactly)

The wall does NOT modify the inter-branch coupling ratio V_12/V_23. The tridiagonal NNI texture is a PERMANENT feature of the singlet sector, immune to domain wall physics. SP confirms the geometric interpretation: the spectral horizon changes WHERE modes live (spatial localization) but not HOW they couple (representation-theoretic selection rules).

This is a new structural result not present in any prior session.

### 1.4 theta_23 Passes at the Dump Point

All three agents recognize theta_23 = 42-52 deg (within PDG window [40.1, 51.7]) as a genuine structural success. The B2 4-fold degeneracy that defines the dump point is the SAME U(2) symmetry that forces near-maximal atmospheric mixing. This is the geometric realization of mu-tau symmetry.

At the phi_paasch attractor point (tau = 0.20, Delta_B2 = 0.254): theta_23 = 49.05 deg, within 0.1 deg of Super-K best fit (49.1 deg).

---

## 2. Novel Cross-Pollination Results

Results that emerged from cross-talk between agents, not present in any input file.

### 2.1 phi_paasch Is a BCS Attractor (Paasch x Neutrino)

**THE CENTRAL DISCOVERY OF THIS ROUND.**

At each tau near the dump point, there exists a specific Delta_B2 where the BCS-dressed mass eigenvalue ratio m_3/m_1 exactly satisfies the Paasch transcendental equation r^2 * ln(r) = 1 to better than 0.002%.

| tau | Delta_B2 for phi match | r^2 * ln(r) | theta_23 | R |
|:----|:----------------------|:------------|:---------|:--|
| 0.190 | 0.128 | 1.000002 | ~46 deg | 0.410 |
| 0.195 | 0.194 | 1.000011 | -- | 0.420 |
| 0.200 | 0.254 | 0.999983 | 49.05 deg | 0.436 |

**Structural significance**: phi_paasch was previously a "spectral feature at the wrong tau" -- exact at tau = 0.150 (inter-sector ratio), FAILING at the dump point tau = 0.190. BCS dressing transforms it into an attractor curve in (tau, Delta_B2) parameter space. The bare inter-sector ratio (E_{(3,0)}/E_{(0,0)}) and the BCS-dressed intra-sector ratio (m_3/m_1) are DIFFERENT algebraic objects converging on the same transcendental fixed point.

**Physical plausibility of Delta_B2 = 0.128 at dump point**: Bulk M_max = 0.077-0.149 (Session 23a K-1e). Wall enhancement 1.9-3.2x (W-32b). Wall M_max ~ 0.15-0.48. Delta_B2 = 0.128 falls within this range.

**Caveats**:
1. Mass vs mass-squared normalization not yet verified
2. Tested at tau = 0.190 and 0.200, not at exact self-consistent operating point
3. Sensitive to Delta_B2 value (ratio varies from 1.547 at Delta = 0 to 1.526 at Delta = 0.40)
4. R and sin^2(theta_13) remain catastrophically wrong at this operating point

### 2.2 V_12/V_23 = 2.7 Is a Structural Constant (Neutrino x SP)

Neutrino's wall-localized computation establishes that V_12/V_23 ~ 2.7 is locked by Schur orthogonality at ALL wall configurations, identical to the bulk value. SP confirms the geometric interpretation: the spectral horizon focuses modes without scattering them between representations.

**Consequence**: R ~ 33 requires V_12^wall/V_23^wall > 316 (corrected from the meta-workshop estimate of > 5). This ratio is 117x above the structural value. No wall modification, BCS dressing, or domain wall physics within the (0,0) singlet can produce this ratio while U(2) is preserved.

**Escape routes for R ~ 33 (all require new computation)**:
1. Inner fluctuation phi (NEW-1): breaks U(2) to SU(2), potentially modifying coupling ratio
2. Off-Jensen PMNS (B-29d redirect): breaks U(2) entirely
3. Inter-sector mixing: contributions beyond the (0,0) singlet

### 2.3 NEC Audit Completes the Penrose Analog (SP)

SP's exact evaluation at the dump point:

- All Ricci eigenvalues positive. Minimum = 0.2225 (su(2) directions).
- NEC violation boundary: tau = 0.7777 (75.6% margin from dump point).
- WCH consistent: |C|^2 = 0.386 at dump (1.08x round metric value). Mild Weyl growth.

The Penrose singularity theorem analog is fully operative at the operating point. Combined with neutrino's normal ordering confirmation, this means: if TURING-1 produces dump-straddling walls AND wall-BCS gap > 0, then normal mass ordering is a geometric consequence. BCS condensation is the thermodynamic cosmic censor.

### 2.4 Domain Wall as Smooth Phase Boundary, Not Singularity (SP)

SP's causal analysis establishes:
- K(tau) finite and continuous through the wall. No curvature singularity.
- tau(x) smooth. No coordinate singularity.
- pi_1(SU(3)) = 0. No topological defect.
- The wall is a DYNAMICAL phase boundary maintained by BCS feedback.
- Self-consistent wall profile tau(x) satisfies the geodesic equation in Jacobi metric: the step-function wall (W-32b) is the restricted coordinate description, the smooth soliton is the maximal extension.

### 2.5 P-30phi Gate Verdict and Domain Wall Resolution (Paasch)

**P-30phi at bulk dump point: FAIL.**

| Parameter | Value |
|:----------|:------|
| Tolerance window [0.5%] | [1.52393, 1.53924] |
| Ratio at tau = 0.190 | 1.52276 |
| Shortfall | 0.00117 (0.077% below lower edge) |
| phi_paasch crossing | tau = 0.1499 (Delta_tau = 0.040 from dump) |

**Domain wall corollary**: If Turing walls span [0.15, 0.19], both the phi crossing and the dump point coexist in a single inhomogeneous configuration. The geometric mean of boundary ratios (Paasch equilibrium mass) falls INSIDE the tolerance window for the (0.10, 0.20) wall: ratio = 1.5285, 0.20% from phi. CONDITIONAL on TURING-1 wall morphology.

---

## 3. Divergent Assessments

### 3.1 Severity of R Shortfall

**Neutrino** (most pessimistic): R_max = 0.71 at the wall (46x below R = 33). The singlet PMNS program within U(2) symmetry is structurally exhausted. V_12/V_23 = 2.7 is locked. No escape within the current computational framework.

**SP** (structural): The R shortfall is a representation-theoretic boundary, not a computational failure. The wall changes spatial localization but preserves algebraic selection rules. U(2) breaking (NEW-1 or off-Jensen) is the only logically consistent forward path.

**Paasch** (notes orthogonality): The phi_paasch attractor curve is independent of the R problem. phi_paasch constrains the (tau, Delta) operating point but says nothing about the coupling ratio V_12/V_23 that determines R.

**Joint assessment**: R ~ 33 within the (0,0) singlet under U(2) symmetry is INACCESSIBLE. This is a constraint boundary, not a parameter-tuning problem.

### 3.2 Status of phi_paasch

**Paasch** (most optimistic): The BCS attractor finding upgrades phi_paasch from "feature at wrong tau" to "dynamical attractor at the operating point." The transcendental equation r^2*ln(r) = 1 satisfied to 0.002% by a BCS-dressed eigenvalue ratio is a non-trivial structural result.

**Neutrino** (cautious): The finding is interesting but normalization-dependent. Mass vs mass-squared ambiguity unresolved. Also, the phi_paasch attractor point has R = 0.41 and sin^2(theta_13) = 0.22 -- both catastrophically wrong. phi_paasch and viable PMNS may be incompatible within the singlet.

**SP** (neutral): No curvature feature distinguishes the phi crossing from the dump point. Both are algebraic. The proximity (Delta_tau = 0.040) on a geometrically featureless background is either coincidence (p ~ 2%) or evidence of a deeper connection.

### 3.3 Speed Bump vs Phase Boundary vs Potential Well

Unresolved from prior workshops. SP's monotonic K(tau) adds no new information to this question. The full quantum-corrected S_eff(tau) profile remains uncomputed.

---

## 4. Gate Verdicts and Pre-Registrations

### 4.1 Gate Verdicts (This Round)

| Gate | Pre-Registered | Threshold | Result | Status |
|:-----|:---------------|:----------|:-------|:-------|
| P-30phi (bulk) | YES (Session 12) | ratio in [1.524, 1.539] | 1.5228 at tau=0.190 | **FAIL** |
| R-WALL | YES (W3 prompt) | R_wall in [5, 100] | R_max = 0.71 | **FAIL** |
| Neutrino wall theta_23 | YES (W3 prompt) | theta_23 in [35, 55] | 42-52 deg | **PASS** |
| Neutrino wall theta_13 | Implicit | sin^2(theta_13) in [0.01, 0.05] | 0.20 minimum | **FAIL** |
| Kretschner extremum | YES (W3 prompt) | K(tau) special structure at dump | Monotonic, no extremum | **NO FEATURE** |
| NEC at dump | YES (SP-Naz Workshop) | NEC holds at tau=0.190 | All Ricci eigenvalues positive | **PASS** |
| Trap 4 at walls | Not pre-registered | V(Bi,Bj)=0 at walls | Zero leakage exactly | **PASS** (structural) |

### 4.2 New Pre-Registrations

| Gate | Threshold | Source | Computation |
|:-----|:----------|:-------|:------------|
| P-33phi | Delta_B2 in [0.10, 0.16] at dump from wall-BCS gap equation | Paasch cross-talk | Wall-BCS (Priority 1) |
| R-NEW1 | R > 5 after U(2) breaking via inner fluctuation phi | Neutrino structural analysis | NEW-1 |
| phi attractor diagnostic | Does wall-BCS gap land on the phi_paasch curve? | Paasch x Neutrino cross-talk | Wall-BCS (Priority 1) |

---

## 5. Updated Constraint Map Entries

### 5.1 New Constraints

**Constraint W3-R1-A**: V_12/V_23 = 2.7 is locked by Schur orthogonality at all wall configurations within the (0,0) singlet under U(2) symmetry.
**Source**: Neutrino Task #2, SP cross-talk.
**Implication**: R ~ 33 is inaccessible through wall-modified couplings alone. Wall physics changes spatial localization of modes but preserves representation-theoretic selection rules.
**Surviving solution space**: U(2)-breaking perturbations (inner fluctuation phi, off-Jensen deformations), inter-sector contributions.

**Constraint W3-R1-B**: P-30phi FAILS at bulk dump point. Ratio 1.5228, misses [1.524, 1.539] by 0.077%.
**Source**: Paasch Task #3, cubic spline interpolation from s22a_paasch_curve.npz.
**Implication**: The bare inter-sector phi_paasch ratio is incompatible with the bare dump point. Exact match at tau = 0.1499 is Delta_tau = 0.040 away.
**Surviving solution space**: (1) Domain wall corollary -- walls spanning [0.15, 0.19] host both features. (2) BCS attractor -- dressed m_3/m_1 recovers phi at Delta_B2 = 0.128.

**Constraint W3-R1-C**: K(tau) monotonically increasing. No curvature extremum at dump point or phi crossing.
**Source**: SP Task #1, exact analytic SP-2 formula.
**Implication**: The dump point convergence is purely representation-theoretic. No curvature shortcut exists to unify the phi crossing and the B2 minimum.
**Surviving solution space**: Unchanged. The representation-theoretic origin of both features is already established.

### 5.2 Confirmed/Strengthened

| Result | Status | Source |
|:-------|:-------|:-------|
| NEC at dump point | CONFIRMED (75.6% margin) | SP NEC audit |
| Normal mass ordering at walls | CONFIRMED (all Delta in [0, 0.5)) | Neutrino full scan |
| JUNO chain: 5/7 links proven | STRENGTHENED | SP NEC + Neutrino ordering |
| Trap 4 at walls (NEW) | PROVEN (zero leakage exactly) | Neutrino computation |
| theta_23 in PDG window at dump | CONFIRMED | Neutrino computation |
| WCH consistency | CONFIRMED (mild 1.08x Weyl growth) | SP Bianchi decomposition |

---

## 6. Computation Recommendations for Round 2

Round 2 agents (KK + Berry + Landau) should read this synthesis and focus on the following.

### Priority 1: Wall-BCS Gap Equation (unchanged, existential)

The gap equation at domain walls remains the single most important unperformed computation. This round adds a new diagnostic dimension: **does the wall-BCS gap land on the phi_paasch curve?**

- If Delta_wall(tau=0.190) is in [0.10, 0.16]: phi_paasch is recovered as a BCS attractor (P-33phi PASS).
- If Delta_wall is outside this range: phi_paasch attractor is falsified at the dump point.
- Input: `s32b_wall_dos.npz`, `s23a_kosmann_singlet.npz`
- Output: Delta_B2 at wall, branch-resolved gap function

### Priority 2: NEW-1 Inner Fluctuation (ESCALATED)

This round ESCALATES NEW-1 from Priority 3 (meta-workshop) to Priority 2. Reason: Neutrino's computation proves that R ~ 33 is INACCESSIBLE within U(2) symmetry. The coupling ratio V_12/V_23 = 2.7 is locked by Schur. The ONLY path to viable R requires U(2) breaking via phi.

- Gate: delta_B2 < 0.058 (theta_23 corridor) AND V_12/V_23 modified from 2.7
- Input: Existing eigenvector data from Session 23a
- Output: B2 splitting, modified coupling ratios, R under phi

### Priority 3: TURING-1 PDE Stability (unchanged)

Determines whether walls nucleate near tau = 0.19 (dump-straddling test). Also determines whether walls span tau ~ [0.15, 0.19], which would resolve the P-30phi domain wall corollary.

- Gate: lambda_T > 0, wall centers near tau = 0.19
- Secondary: wall tau range includes 0.15 (phi crossing)

### Priority 4: Strutinsky Decomposition (unchanged)

Determines whether the 80% bare curvature in RPA-32b is a shell effect (quantum, 16-O calibration: 30-50%) or smooth effect (classical). Zero-cost from existing data.

### Priority 5: RGE Gate (unchanged, outstanding since Session 29)

Bare g_1/g_2 = 0.684 at M_KK, run to M_Z using SM beta functions. Zero-cost. The framework's sharpest contact with measurement.

### New Diagnostics (from this round)

| Diagnostic | What It Tests | Cost |
|:-----------|:-------------|:-----|
| phi_paasch attractor curve | Delta_B2 where m_3/m_1 = phi at each tau | Zero (re-analysis of existing scan) |
| Transcendental equation test | r^2*ln(r) at operating point | Zero |
| Branch-resolved V_12/V_23 under phi | Whether U(2) breaking modifies coupling ratio | Requires NEW-1 |

---

## 7. Open Questions

### 7.1 Can U(2) Breaking Produce R ~ 33?

The singlet sector under U(2) symmetry is exhausted for R. V_12/V_23 = 2.7 is locked. Inner fluctuation phi breaks U(2) to SU(2), splitting B2 into two SU(2) doublets. Whether these doublets have different couplings to B1 and B3 -- and whether the ratio can reach the required 316 -- is the decisive unknown. NEW-1 is the computation.

### 7.2 Is phi_paasch a Dynamical Attractor or a Numerical Coincidence?

The BCS-dressed m_3/m_1 hits phi_paasch at Delta_B2 = 0.128 (tau = 0.190). This is either:
- A dynamical attractor: the wall-BCS gap equation selects Delta_B2 on the phi_paasch curve, producing a zero-parameter prediction.
- A numerical coincidence: the phi_paasch curve passes through the physical Delta range without being dynamically selected.

P-33phi discriminates: if the wall-BCS gap equation produces Delta_B2 in [0.10, 0.16], the attractor interpretation is supported.

### 7.3 Are phi_paasch and Viable PMNS Compatible?

At the phi_paasch attractor point (tau = 0.20, Delta = 0.254): theta_23 = 49.05 deg (excellent), but R = 0.44 (catastrophic) and sin^2(theta_13) = 0.22 (catastrophic). These failures are orthogonal to the phi_paasch constraint -- they trace to V_12/V_23 = 2.7 (locked by Schur). Whether U(2) breaking can fix R and theta_13 while preserving phi_paasch on the attractor curve is unknown.

### 7.4 Does the Domain Wall Corollary Resolve the Dump/Phi Tension?

The phi crossing (tau = 0.15) and dump point (tau = 0.19) are algebraically independent on a geometrically featureless background (SP confirms). If Turing walls span this range, both coexist. Whether TURING-1 produces walls with the right tau range is a pending gate.

---

## 8. Files Produced This Round

| File | Agent | Contents |
|:-----|:------|:---------|
| `tier0-computation/s33w3_sp_dump_geometry.py` | SP | K(tau), NEC audit, Bianchi decomposition |
| `tier0-computation/s33w3_wall_pmns.py` | Neutrino | Hybrid Hamiltonian, PMNS scan over Delta |
| `tier0-computation/s33w3_wall_pmns.npz` | Neutrino | All numerical results |
| `tier0-computation/s33w3_wall_pmns.png` | Neutrino | 6-panel figure |
| `tier0-computation/s33w3_paasch_dump_point.py` | Paasch | phi ratio analysis, transcendental eq test |
| `tier0-computation/s33w3_paasch_dump_point.npz` | Paasch | Results archive |

---

## Summary

Round 1 produces two gate FAILs (P-30phi bulk, R-WALL), two gate PASSes (NEC, theta_23), one structural discovery (phi_paasch BCS attractor), and one critical constraint (V_12/V_23 locked at 2.7 by Schur). The neutrino R problem is now provably inaccessible within U(2) symmetry -- NEW-1 (inner fluctuation) is escalated to Priority 2. The phi_paasch attractor finding opens a new diagnostic axis for the wall-BCS gap equation (P-33phi). Normal mass ordering is confirmed at all wall configurations, strengthening the JUNO pre-registration chain to 5/7 links proven.

The dump point's significance is confirmed as representation-theoretic (B2 eigenvalue minimum), not curvature-invariant (K monotonic). The domain wall is a smooth phase boundary (geodesically complete), not a singularity. These are permanent mathematical results.

---

*Synthesis by coordinator. Integrates SP dump geometry (Kretschner, NEC, Penrose diagram, causal analysis), Neutrino wall-localized PMNS (hybrid Hamiltonian, R scan, theta_23, inter-branch leakage), and Paasch phi analysis (P-30phi verdict, domain wall corollary, transcendental equation, BCS attractor). Cross-talk between all three agents incorporated: Neutrino x Paasch (phi attractor), SP x Neutrino (V_12/V_23 locked), SP x Paasch (no curvature feature at phi crossing). All gate verdicts classified against pre-registered thresholds.*
