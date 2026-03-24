# Session 32 Workshop W4 Round 2: QA x Landau

**Date**: 2026-03-06
**Agents**: qa (quantum-acoustics-theorist), landau (landau-condensed-matter-theorist), coordinator (coordinator)
**Format**: Two-agent workshop with extensive cross-talk. Round 2.
**Mission**: Stress-test R1 findings (slaved gap, shell-crossing pairing, swallowtail trapping, ~1x margin) from acoustic/phononic crystal and condensed matter perspectives. Determine pattern formation mechanism, nucleation dynamics, and superfluid stiffness at domain walls.
**Synthesis Writer**: coordinator

**Input Files**:
- `sessions/session-32/session-32-w4-r1-feynman-nazarewicz.md` (Round 1 synthesis)
- `sessions/session-32/session-32-Team-2-and-3-synthesis.md` (Tesla-LRD-Baptista meta-workshop)
- `sessions/session-32/session-32-Team-4-synthesis.md` (KK-Berry-Landau Round 2)
- `sessions/framework/framework-paasch-potential-master-collab.md` (Paasch wall-intersection master collab)

---

## 1. Convergent Findings

Where both specialists agree after independent analysis and cross-talk. Zero divergences in this workshop.

### 1.1 Slaved Gap = Local Resonance = LK Relaxation (Full Convergence)

R1 established that Delta(x) has no independent dynamics (slaved variable). R2 provides two independent frameworks that confirm and extend this:

**Landau (condensed matter)**: The correct dynamical equation is a single-field Landau-Khalatnikov relaxation:

    Gamma_tau * d(tau)/dt = -dV_eff^{sc}/dtau + (5/2) * nabla^2(tau)

where V_eff^{sc} = V_FR(tau) + eta * V_spec(tau) + E_BCS(tau), with E_BCS(tau) = -Delta^2(tau) * N(tau) / 2 determined locally by the gap equation at each point. The kinetic coefficient K_tau = 5/2 comes from the DeWitt metric (Baptista eq 3.79). The BCS condensation energy is slaved -- it enters the effective potential, not as an independent degree of freedom.

**QA (acoustic/metamaterial)**: Delta(x) is a local resonance whose frequency is set by the lattice parameter tau(x), analogous to a mass-in-mass inclusion in a phononic metamaterial. No gradient term, no wave equation, no independent propagation. The system is in the DISPLACIVE limit of structural phase transitions -- the order parameter follows the lattice parameter adiabatically.

**Joint conclusion**: The system is definitively single-field. Pattern formation proceeds by first-order nucleation at a band-edge-enhanced phase boundary, not by Turing activator-inhibitor instability. At the swallowtail vertex, nucleation simplifies to spinodal decomposition (Section 1.2). This confirms R1's central structural finding and provides the complete dynamical framework.

### 1.2 Swallowtail = Spinodal Decomposition (NUC-1 Trivially Passes)

Landau computed the 3D nucleation barrier B_3D across the parameter space:

| Regime | eta | Coupling | B_3D | Gamma > H? |
|:-------|:----|:---------|:-----|:-----------|
| Swallowtail | 0.04592 | Any | 0 | YES (trivial) |
| Generic, BEC | Generic | V = 0.31 | O(1-10) | YES (B_3D < 18 required) |
| Generic, weak | Generic | V = 0.08 | O(10-50) | MARGINAL |

At the swallowtail vertex (eta = 0.04592), the potential barrier vanishes identically (c_1 = 0 from KK's R2 capstone). The transition is SPINODAL -- no nucleation barrier to overcome. The system undergoes barrierless phase separation throughout the van Hove enhanced region. NUC-1 (the revised TURING-1 gate) PASSES TRIVIALLY.

QA adds: the B2 soft mode goes unstable at the dump point, producing barrierless phase separation. The spinodal wavelength lambda_s ~ 11 M_KK^{-1} sets the initial domain size before coarsening.

**Joint conclusion**: The swallowtail transforms a kinetics problem (nucleation rate) into a thermodynamics problem (free energy minimization). This is a significant simplification from R1's nucleation framing.

### 1.3 Latent Heat Marginally Captures Modulus (L/E_kin Quantified)

Landau's GL coefficients, revised with R1 couplings (V = 0.08-0.31, N_wall = 21.6):

| Quantity | Weak (V = 0.08) | BEC (V = 0.31) |
|:---------|:----------------|:---------------|
| V*N | 1.73 | 6.72 |
| b (quartic GL) | 0.023 | 0.011 |
| c (cubic, L-9) | 0.007 | 0.007 |
| Delta_jump | 0.114 | 0.24 |
| c^2/(4b) | 5.3e-4 | 1.1e-3 |
| L/E_kin (eta = 0.05) | 1.21 | 2.5 |

The latent heat marginally exceeds modulus kinetic energy at weak coupling (20% margin), comfortably exceeds in BEC regime (150% margin). The transition is weakly but genuinely first-order: c^2/(4b) ~ 5e-4 to 1e-3.

QA confirms: Delta_jump = 14-29% of lambda_min, same regime as strong-coupling phonon superconductors (Pb, Hg).

### 1.4 Mean-Field Reliability Confirmed

Two independent measures converge:

**Landau**: Ginzburg number Gi ~ 0.005. Fluctuations are 0.5% of the mean-field order parameter. Comparable to MgB2 (Gi ~ 0.01), 60-200x below MATBG (Gi ~ 0.3-1.0). Mean-field BCS is reliable.

**QA**: Clean-limit hierarchy xi_BCS (0.55) < w_wall (2.0) < l_imp (4.4) [all in M_KK^{-1} units]. Cooper pairs form locally within the wall without impurity suppression. BCS in clean limit.

**Joint conclusion**: Mean-field BCS predictions are trustworthy for this system. No need for beyond-mean-field corrections at the current level of analysis.

### 1.5 M_max ~ O(1) Is Typical for Flat-Band Superconductors

Landau's comparison table places SU(3) B2 in the same M_max/M_crit range as real flat-band materials:

| System | M_max/M_crit | Notes |
|:-------|:-------------|:------|
| MATBG | 1-3 | Flat moire band |
| Kagome AV3Sb5 | 1-2 | Flat Kagome band |
| FeSe/STO | 1-2 | Interface-enhanced |
| SU(3) B2 at wall | 1-2 | Flat B2, van Hove enhanced |

Self-consistency expected to give 2-3x enhancement (MATBG precedent). The R1 margin of ~1x is not anomalously low -- it is TYPICAL for flat-band superconductors before self-consistent treatment.

Three stress tests (Landau):
1. **Van Hove survives BCS**: Coherence peak REINFORCES the fold singularity. M_max not reduced by BCS gap opening.
2. **Ginzburg criterion**: Gi ~ 0.005. Mean-field reliable.
3. **Flat-band comparison**: M_max/M_crit ~ 1-2 is standard.

---

## 2. Novel Cross-Talk Results

Results that emerged from QA-Landau interaction, not present in any input file or in either agent's solo analysis.

### 2.1 CT-1: Quantum Metric Unification of Trapping and Superfluid Stiffness

**Origin**: QA computed the Peotta-Torma geometric superfluid weight; Landau identified the connection to swallowtail trapping. Cross-talk revealed both trace to the same algebraic fact.

Both "any Delta > 0 suffices" results share a single algebraic root: g_B2 = 4.24 (quantum metric).

- **Swallowtail trapping**: The van Hove 1/sqrt singularity comes from d(lambda_B2)/dtau = 0 (flat eigenvalue). At c_1 = 0, the BCS singular attraction always dominates the zero potential slope for any Delta > 0. The fold curvature a_2 = 0.588 is related to g_B2 through the spectral geometry of the B2 band.
- **Superfluid stiffness**: D_s = 2 * g_B2 = 8.48 in the flat-band limit (Peotta-Torma theorem). Independent of Delta magnitude. At the wall (van Hove enhanced): D_s^{wall} ~ 21.

**Root cause**: B2 eigenstates rotate rapidly in Hilbert space (large quantum metric) while eigenvalues remain stationary (flat band). One algebraic fact produces two physical consequences: unconditional trapping at the swallowtail AND Delta-independent superfluid stiffness.

**Status**: Convergent. Connects two previously separate results (KK-Berry swallowtail from R2, Peotta-Torma from QA) through a single algebraic quantity.

### 2.2 CT-2: v_eff = Shell Gap Algebraic Identity

**Origin**: QA discovered the numerical coincidence sqrt(v_B1 * v_B2) = 0.026 = shell gap. Landau proved it is algebraically exact.

For any 2-band system near a fold:
- v_dispersive ~ W (bandwidth)
- v_flat ~ Delta_E^2 / W (second-order perturbation theory)
- sqrt(v_1 * v_2) = Delta_E (trace identity for 2x2 matrices)

**Consequence**: The BCS coherence length is purely a ratio of energy scales: xi_BCS = Delta_E / (pi * Delta). No free parameters.

**Status**: Algebraic identity. Permanent for any 2-band fold system.

### 2.3 CT-3: Clean-Limit Hierarchy

**Origin**: QA computed the length scale hierarchy; Landau provided the nuclear analog.

xi_BCS (0.55) < w_wall (2.0) < l_imp (4.4) [M_KK^{-1} units]

- Coherence length SHORTER than wall width: Cooper pairs form locally within wall (supports slaved gap)
- Mean free path LONGER than coherence length: clean limit, mean-field reliable
- Nuclear analog: drip-line halo nuclei (11Li) where surface-localized pairing occurs with the same hierarchy

**Status**: Convergent. Structural (hierarchy follows from energy scales).

### 2.4 CT-4: Impedance Correction to W-32b M_max

**Origin**: QA's acoustic impedance analysis; Landau endorsed with WKB caveat.

Multiple reflections at wall boundary (R ~ 0.36 from Z_wall/Z_bulk ~ 4) enhance effective DOS by factor 1/(1-R) = 1.56. This pushes R1's M_max lower bound from 0.92 to 1.44.

Landau's caveat: enhancement requires coherent reflections (smooth wall profile). For band-edge B2 modes (k -> 0), the smooth-wall WKB correction exp(-2kw) -> 1, so the enhancement IS valid for the modes that dominate the van Hove DOS.

**Consequence**: R1's "genuinely borderline" verdict on TRAP-1 at singlet level becomes "marginally passes" with impedance correction. The ~1x margin improves to ~1.4x.

**Status**: Convergent. Caveat noted (requires smooth wall, satisfied by KK kink soliton).

### 2.5 CT-5: Displacive Classification

**Origin**: Both agents independently arrived at this classification from different frameworks.

The system is in the DISPLACIVE limit of structural phase transitions:
- QA: Delta is a local resonance parametrically set by tau(x), like a mass-in-mass metamaterial inclusion
- Landau: LK single-field dynamics with Delta slaved to V_eff^{sc}

This is NOT Turing (requires two fields), NOT order-disorder (requires random site occupancy). Pattern formation proceeds by first-order nucleation at the band-edge-enhanced phase boundary. At the swallowtail, this simplifies to spinodal decomposition.

**Status**: Convergent. Classification is permanent (follows from Delta being slaved).

### 2.6 CT-6: Z_wall = 1/pi Universality

**Origin**: QA derived; Landau endorsed.

At any 1D van Hove fold singularity, the acoustic impedance Z = rho * v is FINITE because the DOS divergence (rho ~ 1/(pi*v)) and the velocity vanishing (v -> 0) cancel exactly:

    Z_wall = rho * v = [1/(pi*v)] * v = 1/pi ~ 0.318

This is a universal result for fold catastrophes (A_2 in Thom's classification). The impedance mismatch at the wall boundary: Z_wall/Z_bulk ~ 4, giving reflection coefficient R ~ 0.36. Partial reflection, not total -- BCS coherence extends across the wall boundary.

**Status**: Universal. Structural property of any 1D fold singularity. Permanent.

### 2.7 CT-7: B2 at Dump Point Is a Symmetry-Protected BIC

**Origin**: QA identified the BIC classification in response to Landau's question about flat-band physics at the wall. Landau endorsed.

B2 at the dump point is a BOUND STATE IN THE CONTINUUM (BIC):
- B2 eigenvalue (0.845) lies WITHIN the B3 continuum
- B2 has ZERO coupling to B3 (Trap 4 = Schur orthogonality, exact)
- This is a symmetry-protected BIC with infinite Q-factor
- Protection: U(2) representation theory (B2 = fundamental, B3 = adjoint, inequivalent)

BCS condensation of the BIC = "BIC lasing" in photonic crystal language. The condensate forms in a state that cannot decay into the surrounding continuum.

**Under U(2) breaking** (inner fluctuation phi): the BIC becomes a FANO RESONANCE with finite Q. The Q-factor under phi is an uncomputed quantity relevant to NEW-1.

**Status**: New classification. Not present in any prior session. Structural (follows from Trap 4 + B2 energy position).

### 2.8 CT-8: Type II Wall Classification

**Origin**: Landau computed; QA endorsed.

The wall Ginzburg-Landau parameter:

    kappa_wall = L_wall / xi_BCS = 2.0 / 0.55 = 3.6 >> 1/sqrt(2)

The system is deeply Type II. Consequence: NEGATIVE surface energy at domain walls. Walls PROLIFERATE rather than merge. The optimal configuration is a regular array -- self-consistent with the Z_3 honeycomb wall network picture from prior workshops.

This provides a thermodynamic argument for WHY walls form a regular lattice rather than coarsening into a single domain. The negative surface energy means wall creation is energetically favorable, stabilizing a multi-wall configuration.

**Status**: Convergent. Follows from length scale hierarchy (CT-3).

### 2.9 CT-9: BCS Self-Confinement via Andreev Mirror

**Origin**: QA derived the Andreev reflection coefficient; Landau confirmed the self-confinement feedback loop.

The BCS gap creates a perfect mirror for B2 modes at the wall boundary:

    R_BCS = tanh^2(Delta * w_wall / (2 * v_B2)) ~ 1.0

for Delta ~ 0.11-0.24 (GL Delta_jump values) and w_wall = 2.0, v_B2 = 0.012.

**Positive feedback loop**: BCS condensation -> gap opens -> Andreev mirror forms -> more B2 modes trapped at wall -> larger DOS -> stronger BCS. The condensate is SELF-CONFINING: once formed, it cannot dissolve because the gap prevents B2 escape.

This provides a self-consistency mechanism beyond Nazarewicz's nuclear HFB 2-3x estimate. The Andreev mirror makes the condensate inherently stable against small perturbations.

**Status**: Convergent. Requires TRAP-1 (Delta > 0) as prerequisite.

---

## 3. Divergent Assessments

**None.** This workshop produced zero divergences between QA and Landau. All findings are fully convergent after cross-talk.

The only residual uncertainty is the V normalization (V = 0.08 per-generator vs V = 0.31 full-sum), inherited from R1. Both agents agree this is the dominant uncertainty and that TRAP-1 (4x4 BdG with correct pairing kernel) is the decisive computation.

---

## 4. Corrections to R1

### 4.1 TURING-1 Replaced by NUC-1

**R1 proposed**: Replace "lambda_T > 0" with "Gamma_nucleation > H".

**R2 extends**: At the swallowtail vertex, the nucleation framing is itself unnecessary. The transition is SPINODAL (B_3D = 0), not nucleation. NUC-1 passes trivially. The correct classification is displacive phase separation, not any form of reaction-diffusion instability.

### 4.2 M_max Lower Bound Upgraded

**R1**: M_max = 0.92-2.20 at singlet level. "Genuinely borderline."

**R2**: Impedance correction (CT-4) pushes lower bound from 0.92 to 1.44. Self-consistency expected to give further 2-3x enhancement. "Marginally passes at singlet level" is the corrected assessment.

### 4.3 Pattern Formation Classification Sharpened

**R1**: "Pattern formation by nucleation, not Turing." Correct but incomplete.

**R2**: Pattern formation is DISPLACIVE (CT-5). Three distinct regimes:
- Swallowtail: spinodal decomposition (barrierless)
- Generic eta, BEC: nucleation with moderate barrier (B_3D ~ 1-10)
- Generic eta, weak: nucleation with large barrier (B_3D ~ 10-50, marginal)

### 4.4 Reverse Critical Slowing (New from R2)

**Not in R1.** Landau identifies that the LK relaxation time DECREASES toward the dump point (the BCS singularity steepens V_eff^{sc}). The system ACCELERATES into the BCS minimum, opposite to standard critical slowing near a second-order transition. QA confirms from the acoustic perspective: the dump point is an acoustic absorber, not a reflector. B3 modes (99.6% of RPA weight) provide the dissipation channel.

---

## 5. Combined R1 + R2 Computation Plan

Unified priority list integrating R1 (Feynman x Nazarewicz) and R2 (QA x Landau) findings.

### Priority 1: LANDAU-SECTOR Test (ZERO COST)

**What**: Check whether the B2 eigenvalue minimum at tau ~ 0.19 exists in sectors (1,0), (0,1) from existing .npz data.

**Why decisive**: If universal, multi-sector DOS pushes M_max well above threshold. If singlet-specific, M_max remains at the impedance-corrected ~1.4x margin.

**Pre-registered diagnostic** (from Tesla-LRD-Baptista meta-workshop):
- UNIVERSAL: all sector minima within delta_tau < 0.02 of each other
- SINGLET-SPECIFIC: any minimum shifts by delta_tau > 0.05

**Input**: Sessions 20a/23a .npz files.
**Output**: Sector-resolved B2-analog eigenvalue minima.
**Cost**: Zero (existing data).
**Depends on**: Nothing.
**R2 addition**: If universal, the Type II classification (CT-8) implies walls proliferate across ALL sectors, not just singlet.

### Priority 2: TRAP-1 REVISED -- Multi-Branch BdG at Wall

**What**: Solve multi-branch BdG (B1-B2 cross-shell, 4 B2 modes) at wall using full-sum V_pair from s23a_kosmann_singlet.npz. Include multi-sector DOS from s23a_eigenvectors_extended.npz.

**Pre-registered gates**:
- Delta_wall > 0 (BCS condensation exists)
- M_max > 1 (Thouless threshold)
- At swallowtail (eta = 0.046): any Delta > 0 suffices for trapping

**R2 addition**: Impedance correction (CT-4) enhances effective DOS by 56%. Include in M_max calculation. Gi ~ 0.005 confirms mean-field BdG is the correct tool.

**Input**: s23a_kosmann_singlet.npz, s23a_eigenvectors_extended.npz, s32b_wall_dos.npz.
**Output**: Delta(wall), M_max, trapping verdict.
**Cost**: Medium.
**Depends on**: Priority 1 (LANDAU-SECTOR determines multi-sector contribution).

### Priority 3: Self-Consistent CHFB Wall Profile

**What**: Iterative solution of coupled tau(x)-Delta(x) system. Discretize wall on ~100 grid points. Iterate 15-30 times.

**R2 addition**: LK relaxation provides the dynamical framework. Clean-limit hierarchy (CT-3) validates local BCS at each grid point. Andreev mirror (CT-9) provides self-confinement mechanism that should accelerate convergence.

**Pre-registered gate**: Self-consistent Delta / one-shot Delta > 2 (Nazarewicz nuclear experience).

**Input**: TRAP-1 results + s33w3_modulus_equation.npz (wall profiles).
**Output**: Self-consistent tau(x), Delta(x), convergence history.
**Cost**: Medium-High.
**Depends on**: Priority 2 (TRAP-1 provides starting Delta).

### Priority 4: NUC-1 Nucleation Rate (Replaces TURING-1)

**What**: Compute bubble nucleation rate Gamma for first-order BCS phase transition at the Freund-Rubin barrier.

**R2 finding**: At swallowtail, this gate is trivially satisfied (spinodal, B_3D = 0). At generic eta, B_3D ~ O(1-50) depending on coupling regime. The computation is most needed for the WEAK COUPLING scenario (V = 0.08) where B_3D is largest.

**Pre-registered gate**: Gamma_nucleation > H (B_3D < 18).

**Input**: V_eff from modulus equation, BCS free energy from TRAP-1.
**Output**: Nucleation rate, bubble critical radius, spinodal wavelength.
**Cost**: Medium.
**Depends on**: Priority 2.

### Diagnostics (Zero-Cost)

| Diagnostic | What It Tests | Data Source | R2 Status |
|:-----------|:-------------|:-----------|:----------|
| V_pairing normalization | Full-sum vs per-generator | s23a_kosmann_singlet.npz | STILL DECISIVE (unchanged) |
| Cross-sector V_kk' comparison | Coupling universality | s23a_eigenvectors_extended.npz | Unchanged |
| B1 DOS at wall | B1 enhancement | s32b_wall_dos.npz | Unchanged |
| Superfluid weight D_s | Peotta-Torma at wall | Existing eigenvectors | NEW (CT-1) |
| BIC Q-factor under phi | Fano resonance width | Requires NEW-1 | NEW (CT-7) |

---

## 6. Gate Pre-Registrations

### 6.1 Revised Gates

| Gate | R1 Threshold | R2 Revision | Reason |
|:-----|:-------------|:------------|:-------|
| TURING-1 | Gamma_nucleation > H | REPLACED by NUC-1 | Spinodal at swallowtail makes nucleation rate irrelevant there |
| TRAP-1 | M_max > 1 (Thouless) | M_max > 1 (UNCHANGED, but lower bound now 1.44 with impedance correction) | CT-4 impedance enhancement |

### 6.2 New Pre-Registrations

| Gate | Threshold | Source | Computation |
|:-----|:----------|:-------|:------------|
| NUC-1 | B_3D < 18 at generic eta; trivially 0 at swallowtail | Landau Focus 2 + CT-5 | GL free energy barrier computation |
| GINZBURG-1 | Gi < 0.1 | Landau Focus 4 | PASS (Gi ~ 0.005) -- already satisfied |
| CLEAN-1 | l_imp > xi_BCS | QA + Landau CT-3 | PASS (4.4 > 0.55) -- already satisfied |
| TYPEII-1 | kappa_wall > 1/sqrt(2) | Landau CT-8 | PASS (kappa = 3.6) -- already satisfied |

### 6.3 Gates Already Satisfied (from R2 analysis)

| Gate | Value | Threshold | Status |
|:-----|:------|:----------|:-------|
| GINZBURG-1 | Gi ~ 0.005 | < 0.1 | PASS |
| CLEAN-1 | l_imp/xi_BCS = 8.0 | > 1 | PASS |
| TYPEII-1 | kappa = 3.6 | > 0.707 | PASS |
| NUC-1 (swallowtail) | B_3D = 0 | < 18 | PASS (trivial) |

---

## 7. Constraint Map Updates

### 7.1 New Constraints

**Constraint W4-R2-A**: Z_wall = 1/pi at any 1D van Hove fold. DOS divergence and velocity vanishing cancel exactly. Impedance mismatch Z_wall/Z_bulk ~ 4, reflection R ~ 0.36.
**Source**: QA acoustic analysis, Landau endorsed.
**Implication**: Wall boundaries are PARTIALLY reflecting, not totally. BCS coherence extends across walls.
**Surviving solution space**: Unchanged (positive -- coherence is maintained).

**Constraint W4-R2-B**: Superfluid weight D_s = 2 * g_B2 = 8.48, INDEPENDENT of Delta magnitude. Peotta-Torma flat-band saturation theorem.
**Source**: QA (Peotta-Torma framework), Landau endorsed.
**Implication**: Condensate stiffness is set by quantum metric (eigenstate rotation), not by gap size. Nonzero for any Delta > 0.
**Surviving solution space**: Any Delta > 0 gives finite superfluid stiffness.

**Constraint W4-R2-C**: Clean-limit hierarchy xi_BCS (0.55) < w_wall (2.0) < l_imp (4.4). Gi ~ 0.005.
**Source**: QA (length scales) + Landau (Ginzburg number). Convergent.
**Implication**: Mean-field BCS is reliable. No impurity destruction. Local pairing within wall.
**Surviving solution space**: Standard BCS applies without beyond-mean-field corrections.

**Constraint W4-R2-D**: NUC-1 PASSES trivially at swallowtail (spinodal decomposition, B_3D = 0). Marginal at generic eta weak coupling (B_3D ~ 10-50).
**Source**: Landau GL computation.
**Implication**: Pattern formation is barrierless at the swallowtail vertex. No nucleation bottleneck.
**Surviving solution space**: Swallowtail vertex is strongly favored for mechanism viability.

**Constraint W4-R2-E**: Latent heat L/E_kin = 1.21 (weak coupling) to 2.5 (BEC) at eta = 0.05.
**Source**: Landau GL coefficients with R1 couplings.
**Implication**: Modulus kinetic energy is marginally absorbed at weak coupling (20% margin), comfortably absorbed in BEC (150%).
**Surviving solution space**: V normalization determines which regime applies.

**Constraint W4-R2-F**: B2 at the dump point is a symmetry-protected BIC (bound state in continuum). Energy within B3 continuum, zero coupling via Trap 4. Infinite Q-factor.
**Source**: QA identification, Landau endorsed. Cross-talk product.
**Implication**: BCS condensation occurs in a state that cannot decay into the surrounding continuum. Would become Fano resonance under U(2) breaking (phi).
**Surviving solution space**: BIC classification is structural (Trap 4). Q-factor under phi requires NEW-1.

**Constraint W4-R2-G**: BCS gap creates Andreev mirror (R_BCS ~ 1.0). Condensate is self-confining via positive feedback: BCS -> gap -> mirror -> more trapping -> stronger BCS.
**Source**: QA (Andreev reflection coefficient) + Landau (feedback loop identification). Convergent.
**Implication**: Once BCS condensate forms at the wall, it is inherently stable against dissolution.
**Surviving solution space**: Requires TRAP-1 (Delta > 0) as prerequisite.

**Constraint W4-R2-H**: Reverse critical slowing at the dump point. LK relaxation time DECREASES (not increases) toward tau = 0.19. System accelerates into the BCS minimum.
**Source**: Landau LK computation + QA acoustic absorber identification. Convergent.
**Implication**: No kinetic bottleneck at the dump point. Modulus falls into BCS trap rapidly.
**Surviving solution space**: Unchanged (positive -- no kinetic obstacle).

**Constraint W4-R2-I**: Domain correlation length L ~ 0.35 M_KK^{-1} << wall width 1.3-2.7. Walls are sharp phase boundaries.
**Source**: Landau LK relaxation.
**Implication**: Phase boundaries are well-defined, not diffuse. Supports the kink soliton picture from KK R2.
**Surviving solution space**: Unchanged.

**Constraint W4-R2-J**: Type II wall classification. kappa_wall = L_wall/xi_BCS = 3.6 >> 1/sqrt(2). Negative surface energy. Walls proliferate.
**Source**: Landau, QA endorsed.
**Implication**: Thermodynamic argument for wall lattice formation. Multi-wall configuration energetically favored over single domain.
**Surviving solution space**: Z_3 honeycomb network is the thermodynamically preferred state.

**Constraint W4-R2-K**: v_eff = sqrt(v_B1 * v_B2) = Delta_E (shell gap). Algebraic identity for 2-band fold systems.
**Source**: QA discovery, Landau proof (trace identity for 2x2 matrices).
**Implication**: BCS coherence length xi_BCS = Delta_E/(pi*Delta) is parameter-free.
**Surviving solution space**: Unchanged (structural identity).

**Constraint W4-R2-L**: Impedance correction pushes R1 M_max lower bound from 0.92 to 1.44.
**Source**: QA Fabry-Perot analysis, Landau endorsed with WKB caveat.
**Implication**: Singlet-only M_max marginally passes threshold even without multi-sector contributions.
**Surviving solution space**: LANDAU-SECTOR test remains important for margin but no longer existential at singlet level.

### 7.2 R1 Constraints Updated

| R1 Constraint | R2 Update |
|:-------------|:----------|
| W4-R1-A (M_max = 0.92-2.20, ~1x) | Lower bound upgraded to 1.44 via impedance correction (CT-4). Self-consistency expected to give further 2-3x. |
| W4-R1-B (Delta slaved) | CONFIRMED and EXTENDED to displacive classification (CT-5) and LK single-field equation. |
| W4-R1-C (B1-B2 shell-crossing) | CONFIRMED. v_eff = shell gap identity (CT-2) provides algebraic foundation. |
| W4-R1-D (R2 100-500x retracted to ~1x) | CONFIRMED retracted. Impedance correction partially restores margin to ~1.4x. |

### 7.3 Prior Workshop Constraints Updated

| Prior Constraint | R2 Update |
|:----------------|:----------|
| W3-R2-F (Delta_crit ~ 0.07-0.10) | Refined: Delta_jump = 0.114-0.24 from GL (first-order, c/b ratio). Delta_jump exceeds Delta_crit in BEC regime. |
| W3-R2-H (barrier-fold merger at eta = 0.04592) | STRENGTHENED. At swallowtail: spinodal (CT-5), reverse critical slowing (W4-R2-H), self-confinement (CT-9). Three independent mechanisms reinforce trapping. |
| W3-R2-I (binary 100x/10^{-4}) | STILL BINARY but impedance correction narrows the gap between regimes. |
| W3-R2-J (swallowtail unconditional) | CONFIRMED with additional mechanisms: spinodal + reverse slowing + Andreev mirror + BIC protection. |

---

## 8. Open Questions

### 8.1 V_pair Normalization (Inherited from R1, STILL DECISIVE)

V = 0.08 (per-generator) vs V = 0.31 (full-sum) determines whether the system is in weak coupling (L/E_kin = 1.21, marginal) or BEC (L/E_kin = 2.5, comfortable). TRAP-1 computation with the correctly projected pairing kernel resolves this.

### 8.2 Does the Spinodal Wavelength Set the Domain Size?

Landau estimates lambda_s ~ 11 M_KK^{-1} as the initial domain size from spinodal decomposition. Subsequent coarsening dynamics (Lifshitz-Slyozov) would modify this. The equilibrium domain size is set by competition between wall surface tension and Z_3 topological constraints, not by lambda_s.

### 8.3 BIC -> Fano Resonance Under Phi?

The B2 BIC (CT-7) has infinite Q protected by U(2). Inner fluctuation phi breaks U(2) to SU(2), making the BIC a Fano resonance with finite Q. What is the Q-factor? This is relevant to NEW-1 and to whether BCS condensation survives phi.

### 8.4 Does Andreev Self-Confinement Affect the CHFB Convergence Rate?

The positive feedback loop (CT-9) suggests self-consistent iteration may converge faster than the 15-30 iterations estimated from nuclear CHFB. The Andreev mirror makes each iteration self-reinforcing.

---

## 9. Updated Phonon-NCG Dictionary Entries

### From This Workshop (NEW)

| NCG / Spectral Geometry | Phononic Crystal / Condensed Matter | Source |
|:------------------------|:------------------------------------|:-------|
| B2 at dump point | Symmetry-protected BIC in B3 continuum | CT-7 |
| BCS gap at wall | Andreev mirror / acoustic band gap | CT-9 |
| LK relaxation at dump | Acoustic absorber (reverse critical slowing) | CT-8, Landau Focus 1 |
| Swallowtail vertex | Spinodal decomposition point | CT-5, Landau Focus 2 |
| Delta(x) slaved | Local resonance in metamaterial (displacive) | CT-5, QA Focus 4 |
| kappa_wall = 3.6 | Type II (negative surface energy, walls proliferate) | CT-8 |
| D_s = 2*g_B2 | Peotta-Torma geometric superfluid weight | CT-1 |
| v_eff = shell gap | Two-band trace identity | CT-2 |

---

## 10. Self-Corrections During Workshop

### None Required

Both agents converged on all findings without significant self-corrections. QA's initial impedance estimate was refined (not corrected) by Landau's WKB caveat. No retractions, no errors identified.

This is notable: R1 had multiple self-corrections (Feynman exchange retraction, V normalization resolution, 100-500x margin correction). R2 built on the corrected R1 results without introducing new errors.

---

## Summary

This workshop produced zero divergences and nine novel cross-talk results from the QA-Landau interaction. The central finding is the **quantum metric unification** (CT-1): the algebraic quantity g_B2 = 4.24 is the single root cause of both swallowtail trapping (fold singularity -> unconditional trapping for any Delta > 0) and superfluid stiffness (Peotta-Torma D_s = 2*g_B2 = 8.48, Delta-independent).

Three findings upgrade R1's assessment:
1. **M_max lower bound 0.92 -> 1.44** via impedance correction (CT-4), changing "genuinely borderline" to "marginally passes at singlet"
2. **NUC-1 trivially passes** at swallowtail via spinodal decomposition (Landau Focus 2), eliminating the nucleation bottleneck entirely
3. **BCS self-confinement** via Andreev mirror (CT-9) provides a stability mechanism beyond the bare potential argument

Two new physical classifications for the dump point:
1. **B2 is a symmetry-protected BIC** (CT-7) -- bound state in the continuum, infinite Q from Trap 4
2. **Type II wall** (CT-8) -- negative surface energy, walls proliferate thermodynamically

The mechanism chain's fate still reduces to TRAP-1 (4x4 BdG with correct pairing kernel). The V normalization (0.08 vs 0.31) remains the dominant uncertainty. Everything else is structurally robust and mutually consistent between the acoustic and condensed matter perspectives.

---

*Synthesis by coordinator. Integrates QA's acoustic/phononic crystal analysis (impedance universality, superfluid weight saturation, clean-limit hierarchy, local resonance classification, Fabry-Perot DOS enhancement, BIC identification) and Landau's condensed matter analysis (LK relaxation, nucleation dynamics, GL coefficients, Ginzburg criterion, flat-band comparison, Type II classification). Nine cross-talk results (CT-1 through CT-9) emerged from mutual interaction. All findings convergent. No divergences. No self-corrections. Twelve new constraints (W4-R2-A through L). Four R1 constraints updated. Four prior workshop constraints updated.*
