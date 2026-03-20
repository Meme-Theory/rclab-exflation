# Session 32 Workshop: Hawking x Cosmic-Web Cross-Pollination

**Date**: 2026-03-04
**Agents**: hawking (hawking-theorist), cosmic-web (cosmic-web-theorist), coordinator
**Input Files**:
- `sessions/session-32/session-32-hawking-collab.md`
- `sessions/session-32/session-32-cosmic-web-collab.md`
**Format**: 5-topic cross-pollination workshop with multi-round exchange
**Synthesis Writer**: coordinator

---

## 1. Convergent Findings

Where thermodynamic/semiclassical (Hawking) and condensed matter/superfluid (Cosmic-Web) perspectives agree, after multi-round exchange with self-corrections.

### 1.1 Domain Wall Is a Passive Trap with Subdominant Active Component (Topic 1)

Both agents converge on the physical classification of the domain wall: it is a PASSIVE van Hove trap (spectral weight concentration from reduced group velocity), NOT an active Hawking-like particle source. The active Bogoliubov component is subdominant by a factor of 20-100x.

**Semiclassical argument** (Hawking): No causal horizon exists at the domain wall. Both sides of the wall are accessible -- there is no trace over interior degrees of freedom. Without a trace, the Planckian factor exp(-2*pi*omega/kappa) does not arise (Paper 05, Hawking 1975). The spectrum is non-thermal (confirmed Session 29Ac, Parker mechanism). The mode-trapping kinematics parallel Hawking radiation, but the thermodynamics do not.

**Condensed-matter argument** (Cosmic-Web): Calibrated against 3He A-B interface Andreev reflection (r_A ~ 0.3-0.8 at gap edge). Framework eigenvector overlaps 0.21-0.87 translate to |beta|^2 ~ 0.01-0.05 after J decomposition into particle-antiparticle blocks. The van Hove DOS enhancement (rho_wall = 12.5-21.6) is 20-100x larger than the Bogoliubov production rate. The wall concentrates existing spectral weight rather than creating new particles.

**Joint conclusion**: The mechanism chain operates via passive spectral weight concentration, not active particle creation. Back-reaction is CONSTRUCTIVE (BCS condensation reinforces wall geometry), not destructive (Hawking evaporation dissolves horizon). This is physically crucial for mechanism chain persistence.

### 1.2 Trans-Planckian Universality Extends to Domain Walls (Topics 1, 3)

Both agents agree that the van Hove enhancement at domain walls inherits the UV-robustness established for the spectral action (H-5 CONFIRMED, Session 25), but from a DIFFERENT universality class than Hawking radiation.

**Semiclassical argument** (Hawking): Paper 05 proves the thermal spectrum depends only on the surface gravity kappa, not on UV physics. The domain wall DOS depends only on v_group near the wall, not on high-energy mode structure. Both are instances of near-feature universality. Testable: compute wall DOS at N_max = 4, 5, 6 and verify convergence.

**Condensed-matter argument** (Cosmic-Web): Van Hove singularities are classified by the codimension of the degeneracy manifold in k-space (van Hove 1953). The classification is topological and insensitive to microscopic details.

**Two universality classes identified**: Hawking universality is CONFORMAL (depends on near-horizon conformal structure). Van Hove universality is TOPOLOGICAL (depends on codimension of degeneracy manifold). Both UV-robust, different mathematical origins.

### 1.3 The Quantum Metric Is Nonlocal Vacuum Polarization (Topic 3)

Both agents agree on the thermodynamic interpretation of the Connes-QA quantum metric identity (Workshop Result 1 from the Connes x QA workshop): the 20.7% off-diagonal contribution to chi = 20.43 is BEYOND the Seeley-DeWitt derivative expansion.

**Semiclassical argument** (Hawking): The 79.3% bare curvature IS the local Euler-Heisenberg effective Lagrangian. The 20.7% shell correction is the spectral-action analog of nonlocal back-reaction in Hawking radiation (Paper 06). Wall 4 (V_spec monotonicity, Session 24a V-1) used only the LOCAL Seeley-DeWitt terms. RPA-32b reverses the conclusion via the NONLOCAL quantum metric contribution. Same mathematical structure as the Hawking information paradox resolution: local analysis says monotone, nonlocal correction reverses the sign.

**Condensed-matter argument** (Cosmic-Web): The quantum metric controls superfluid weight in flat-band systems (Peotta-Torma 2015). The spectral action shell correction IS the geometric stiffness that guarantees the B2 condensate has nonzero superfluid weight despite vanishing group velocity. The RPA result (Q ~ 3000, weakly screened) confirms the system is in the regime where the quantum metric contribution is most reliable.

**Joint conclusion**: The local/nonlocal decomposition (79.3% / 20.7%) is the spectral-action analog of the tree-level/one-loop decomposition in semiclassical gravity. The nonlocal piece circumvents Wall 4 and simultaneously encodes the geometric superfluid weight. Status: mathematical identity (from Connes-QA), thermodynamically grounded (this workshop).

### 1.4 BCS-First Priority Ordering (Topic 5)

Both agents converge on the Session 33 priority ordering after initial disagreement (see Section 3.1).

**Final jointly agreed priority list**:
1. Wall-BCS gap equation (decisive for mechanism chain)
2. TURING-1 PDE stability (decisive for volume fraction, contingent on #1)
3. Bogoliubov |beta|^2 extraction from W-32b (low-cost, active/passive)
4. Im(Sigma) quasiparticle lifetime at wall (one-line addition to #1)
5. GSL three-term entropy check (zero-cost from existing data)
6. Euclidean action minimum at dump point (low-cost, no-boundary connection)

**Logic** (Hawking, accepted by Cosmic-Web): "First the mechanism, then the census" (Paper 05, 1975 -> Carr 1976). Wall-BCS tells us WHETHER condensation works at a single wall. TURING-1 tells us HOW MANY walls exist. If BCS fails, wall count is irrelevant.

### 1.5 Dump Point Self-Consistency (Topics 2, 5)

Both agents identify the dump point tau = 0.190 as the OPTIMAL location for wall stability. The spectral action curvature is maximized (chi = 20.43), wall width is minimized, and all seven convergent quantities trace to the B2 eigenvalue minimum. This self-consistency is a zero-parameter result: the operating point of the mechanism chain is fixed by group theory (SO(8) -> U(2) symmetry breaking).

**Cosmic-Web framing**: The dump point is where Turing wall stability is strongest (Delta_F maximized, xi_wall minimized). Self-consistent: the B2 eigenvalue minimum determines both the operating point and the wall stability.

**Hawking framing**: The dump point may be selected by the no-boundary wave function Psi ~ exp(-I_E). If I_E + I_E^{one-loop} has a minimum at tau ~ 0.19, Hartle-Hawking (Paper 09) selects the dump point as the preferred initial configuration. STATUS: CONJECTURE, requires Euclidean action computation (Priority 6).

---

## 2. Novel Workshop Results

Five genuinely new results emerged from the cross-pollination, none of which appeared in either input collab file alone.

### 2.1 Result 1: Mode-Trapping Continuum

**Statement**: Hawking radiation and domain-wall van Hove enhancement are the v_group = 0 and v_group = epsilon limits of a SINGLE mechanism -- spectral weight concentration from group velocity reduction. The thermal/non-thermal transition is a phase transition in the spectrum parametrized by v_group.

**Four structural differences between the two limits**:

| Feature | Hawking (v_group = 0) | Domain Wall (v_group = epsilon) |
|:--------|:----------------------|:-------------------------------|
| Spectral character | Thermal (Planckian) | Non-thermal (Parker) |
| Back-reaction sign | Destructive (evaporative) | Constructive (stabilizing) |
| Information content | Exponentially scrambled | Algebraically determined (overlaps 0.21-0.87) |
| Quasiparticle lifetime | Infinite (escape to infinity) | Finite (scattering via off-diagonal V matrix) |

**Transition physics**: At v_group = 0, tracing over the interior becomes mandatory (Unruh, Paper 12), producing the Planckian spectrum. At v_group = epsilon, modes slow but do not become causally disconnected, producing a non-thermal spectrum. The transition is sharp, not gradual.

**Significance**: Unifies two apparently distinct mechanisms (Hawking particle creation and van Hove DOS enhancement) as limits of a single spectral phenomenon. The framework operates firmly in the non-thermal (passive, constructive) regime.

**Status**: Joint conceptual result. Well-posed. Grounded in Unruh (Paper 12) and van Hove (1953).

### 2.2 Result 2: Three-Term GSL Accounting

**Statement**: The generalized second law at domain walls requires tracking three entropy contributions, not two.

- **Term 1**: Spectral entropy decrease, delta S_spec < 0 (monotonically decreasing, H-2 Session 25). Magnitude: O(1).
- **Term 2**: Bogoliubov particle entropy, delta S_particles > 0 (enhanced at wall by factor R = 1.5-3.7x of |Term 1|, Session 29a).
- **Term 3**: BCS condensation entropy, delta S_condensate < 0 (pure state, S = 0 -- entropy REDUCTION from pre-condensation mixed state).

**GSL requirement**: delta(S_spec + S_particles + S_condensate) >= 0 globally. Tighter constraint than the bulk case (Session 29a) because Term 3 is new and negative.

**Free energy ratio**: Delta_F / T_eff ~ 0.5-2.0 (dimensionless). The wall is MARGINALLY stable against thermal fluctuations. This is the thermodynamic bottleneck of the mechanism chain, complementing the kinematic bottleneck (W-32b margin 1.9-3.2x). Both bottlenecks trace to the same algebraic root (B2 eigenvalue minimum).

**Stronger form** (Hawking, speculative): Island-formula bound delta_S >= delta_A_wall / (4*G_eff) (Paper 14, Penington 2019). Requires gravitational theory in internal space. Flagged as theoretical target, NOT a Session 33 gate.

**Weaker form** (adopted gate): R_total = delta_S_particles / |delta_S_spec + delta_S_condensate| >= 1. This is the Session 33 GSL gate.

**Status**: Joint formulation. Quantitative estimate from existing data. Gate pre-registered for Session 33.

### 2.3 Result 3: Bogoliubov-Lindhard Synthesis

**Statement**: The Bogoliubov coefficients (scattering amplitudes, mode mixing across wall) and the Lindhard function (ground-state screening, collective response) are DIFFERENT physical observables encoded in the SAME eigenvector overlap matrix U_{ij} = <psi_i(tau_1)|psi_j(tau_2)> from W-32b.

- **Lindhard** = forward scattering (diagonal of U*U^dagger). Already extracted: chi_Lindhard = -1.059 (6.5% of total curvature).
- **Bogoliubov** = off-diagonal mode mixing. NOT YET extracted. Extractable at zero cost from existing data.

**Joint extraction criterion**: Decompose U_{ij} into particle-particle (alpha) and particle-antiparticle (beta) blocks using the J operator. Trap 5 constrains: B1/B3 beta is REAL (J maps within the same multiplet), B2 beta is COMPLEX (J maps fundamental to anti-fundamental).

**Physical answers from the decomposition**:
- |beta|^2 spectrum answers Hawking's question: active vs passive?
- Andreev reflection coefficient answers Cosmic-Web's question: what fraction of incident modes reflect as antiparticles at the wall?
- Predicted: |beta|^2 ~ 0.01-0.05 (3He calibration). Passive-dominant.

**Status**: Joint result. Zero-cost computation from existing s32b_wall_dos.npz data. Recommended as Session 33 Priority 3.

### 2.4 Result 4: Sound Speed and Wall Effective Temperature

**Statement**: The quantum metric ratio gives a concrete prediction for the sound speed of fluctuations propagating along a domain wall:

    c_eff^2 ~ g_B2 / chi_bare ~ 4.24 / 16.19 ~ 0.26
    c_eff ~ 0.51 (spectral-action units)

**Thermodynamic connection** (Hawking): The wall effective temperature is T_GH ~ hbar * c_eff / (2*pi * w_wall), analogous to the Gibbons-Hawking temperature of de Sitter space (Paper 07). This links directly to the BCS survival criterion.

**BCS survival gate**: T_GH < Delta_BCS. Equivalently, the quasiparticle lifetime tau_qp > hbar/Delta_BCS. If violated, the condensate melts at the wall and the mechanism chain is self-defeating.

**Superfluid density prediction** (Hawking, pre-registered for Session 33):

    rho_s(B2) = (2 * Delta_BCS / V_cell) * g_B2 = (2 * Delta_BCS / V_cell) * 4.24

If BCS-at-walls yields Delta_BCS, this immediately gives the London penetration depth and gauge boson mass at the wall.

**Status**: Quantitative prediction from existing data. Testable once Delta_BCS is computed. Connects quantum metric identity (Connes-QA) to thermodynamic stability (this workshop).

### 2.5 Result 5: Volume Fraction Estimate with Bekenstein Bound

**Statement**: The volume fraction of domain walls f_wall has both upper and lower bounds from independent physics.

**Lower bound** (Cosmic-Web): BCS threshold requires rho >= rho_crit = 6.7 (from K-1e). The wall DOS rho_wall = 12.5-21.6 satisfies this, but only WITHIN the wall. Cosmological relevance requires f_wall > f_min ~ 0.01 (1%).

**Upper bound** (Hawking): Bekenstein bound S_cell <= 2*pi * R * E_cell (Paper 11, Bekenstein 1973). The quasiparticle entropy per Turing cell cannot exceed the Bekenstein limit. Combined with the BCS threshold (minimum DOS per cell), this gives f_wall < f_max.

**Estimate** (Cosmic-Web): f_wall ~ 0.01-0.1 (1-10%). Above 3He analog (f ~ 10^{-3}) because:
- Small D_B2 (flat band, slow diffusion) narrows Turing spacing
- Large chi_spectral = 20.43 narrows wall width

Both effects push f_wall upward relative to condensed-matter analogs.

**Self-consistency**: If the allowed window (f_min, f_max) is nonempty, the mechanism chain is thermodynamically self-consistent. If Bekenstein upper < BCS lower, the mechanism is thermodynamically forbidden.

**Status**: Estimate from condensed-matter calibration + thermodynamic bound. TURING-1 computation is decisive for the actual value.

---

## 3. Divergent Findings

### 3.1 Priority Ordering: BCS-First vs Turing-First (Resolved)

**Hawking position**: Wall-BCS gap equation should be Session 33 Priority 1, with TURING-1 contingent on BCS passing. Logic: "first the mechanism, then the census." If condensation fails at a single wall, counting walls is irrelevant.

**Cosmic-Web initial position**: TURING-1 should be Priority 1 because the volume fraction is the ultimate discriminator for cosmological relevance. If f_wall << 0.01, even a working BCS mechanism is irrelevant.

**Resolution**: Cosmic-Web conceded the BCS-first ordering. The logical chain is sequential: mechanism confirmation THEN census. Both are Session 33 priorities; only the ordering changed.

### 3.2 Island Formula: Rigorous Gate vs Theoretical Target

**Hawking**: Proposed the stronger island-formula bound delta_S >= delta_A_wall / (4*G_eff) as a GSL gate. Grounded in Penington (Paper 14) and the identification of the domain wall as a quantum extremal surface in the internal space.

**Cosmic-Web**: Flagged as speculative because it requires an effective gravitational theory in the internal space, which the framework does not derive (Channel 2 closed, Session 29). The weaker form R >= 1 is sufficient and computable from existing data.

**Resolution**: Weaker form R >= 1 adopted as the Session 33 gate. Stronger island-formula form remains a theoretical target for future work if/when G_eff in the internal space is derived.

### 3.3 Thermal Stability: Marginal vs Safe

**Hawking**: The free energy ratio Delta_F / T_eff ~ O(1) is "not parametrically safe." The wall is marginally stable. The BCS gap equation at the wall must demonstrate that Delta_BCS exceeds the effective wall temperature T_GH.

**Cosmic-Web**: The O(1) estimate is consistent with 3He analog (A-B interface is also marginally stable, yet survives experimentally at T/T_c > 0.5). The dump point self-consistency (chi maximized at tau = 0.190) provides an extra margin not captured in the dimensionless ratio.

**Status**: Not resolved. Both acknowledge the marginal stability. The BCS gap equation (Session 33 Priority 1) is the decisive computation.

---

## 4. Joint Computation Recommendations for Session 33

Ranked by priority, with justification from both perspectives. All six use existing data from `s32b_wall_dos.npz` and `s32b_rpa1_thouless.npz`.

### Priority 1: Wall-BCS Gap Equation

**What**: Solve the BCS gap equation with wall-localized DOS from W-32b (rho_wall = 12.5-21.6), replacing the bulk DOS from K-1e (Session 23a). Include Im(Sigma) quasiparticle lifetime check.

**Semiclassical justification** (Hawking): The wall-BCS gap equation determines whether the vacuum polarization (RPA-32b) translates into an actual condensate. This is the analog of computing whether the Euler-Heisenberg effective action produces a non-perturbative vacuum decay (Schwinger mechanism). The quasiparticle lifetime gate (tau_qp > hbar/Delta_BCS) ensures the condensate is not self-defeating.

**Condensed-matter justification** (Cosmic-Web): Standard BCS with modified DOS. The 1.9-3.2x margin above K-1e threshold (rho_crit = 6.7) must translate into a nonzero Delta_BCS. The Im(Sigma) check (one-line addition) verifies quasiparticle stability.

**Pre-registered gate**: Delta_BCS > 0 with rho = rho_wall. PASS if nonzero. FAIL if the enhanced DOS still does not overcome the spectral gap.

**Input**: `s32b_wall_dos.npz` (wall DOS), `s23a_kosmann_singlet.npz` (coupling matrix).
**Output**: Delta_BCS at the wall, quasiparticle lifetime tau_qp.

### Priority 2: TURING-1 PDE Stability Analysis

**What**: Full linear stability analysis of the reaction-diffusion PDE with B1+B2+B3 diffusion and V_{ij} interaction terms. Determine the Turing wavelength, growth rate, and spatial pattern morphology.

**Semiclassical justification** (Hawking): Contingent on Priority 1 passing. Determines how many walls exist and therefore the cosmological relevance of the BCS mechanism.

**Condensed-matter justification** (Cosmic-Web): The extreme diffusion ratio D_B3/D_B2 ~ 3435 (344x above Turing threshold) predicts deep supercritical pattern formation. The wavelength determines the volume fraction f_wall. The Hessian eigenvalue classification (van de Weygaert, Paper 03) determines morphology (sheets vs filaments vs bubbles).

**Pre-registered gate**: Turing wavelength lambda_T is finite. PASS if lambda_T > 0. FAIL if no instability (all growth rates negative).

**Input**: `s32b_rpa1_thouless.npz` (V matrix, diffusion coefficients), U-32a sign structure.
**Output**: lambda_T, growth rate sigma_max, pattern morphology, volume fraction estimate.

### Priority 3: Bogoliubov |beta|^2 Extraction

**What**: Decompose the W-32b eigenvector overlap matrix U_{ij} into particle-particle (alpha) and particle-antiparticle (beta) blocks using J. Extract |beta|^2 spectrum by branch.

**Joint justification**: Zero-cost post-processing of existing data. Simultaneously resolves: (a) active vs passive wall classification, (b) Andreev reflection coefficient, (c) Trap 5 constraint on B1/B3 beta (must be real).

**Input**: `s32b_wall_dos.npz` (eigenvector overlaps), J operator from existing Dirac data.
**Output**: |beta|^2 spectrum by branch. Binary: passive-dominant (|beta|^2 << 1) or active (|beta|^2 ~ 1).

### Priority 4: Im(Sigma) Quasiparticle Lifetime

**What**: Compute the imaginary part of the self-energy at the domain wall. One-line addition to Priority 1.

**Joint justification**: The quasiparticle lifetime tau_qp = hbar / Im(Sigma) must exceed the BCS formation time hbar/Delta_BCS. If tau_qp < hbar/Delta_BCS, quasiparticles decay before they can pair, and the condensate cannot form.

**Pre-registered gate**: tau_qp > hbar/Delta_BCS. Equivalently, T_GH < Delta_BCS.

**Input**: Same as Priority 1.
**Output**: Im(Sigma) at wall, tau_qp.

### Priority 5: GSL Three-Term Entropy Check

**What**: Compute the three-term entropy balance (delta S_spec + delta S_particles + delta S_condensate) at domain wall configurations. Verify GSL: total entropy change >= 0.

**Joint justification**: Zero-cost from existing data. Extends Session 29a bulk entropy balance (R = 1.53-3.67) to the inhomogeneous case. The marginal thermal stability estimate (Delta_F / T_eff ~ O(1)) makes this a non-trivial check.

**Pre-registered gate**: R_total >= 1. FAIL if entropy decreases globally.

**Input**: `s32b_wall_dos.npz` (wall DOS), Session 29a entropy formula.
**Output**: R_total at three wall configurations.

### Priority 6: Euclidean Action Minimum at Dump Point

**What**: Evaluate I_E + I_E^{one-loop} at tau = 0.19 and compare to tau = 0. Test whether the quantum-corrected Euclidean action has a local minimum near the dump point.

**Semiclassical justification** (Hawking): If I_E has a minimum at tau ~ 0.19, the no-boundary wave function Psi ~ exp(-I_E) selects the dump point as the preferred initial configuration (Paper 09, Hartle-Hawking 1983). The bare I_E is monotonically decreasing (H-1, Session 25). RPA-32b adds positive curvature. Is the correction large enough to create a minimum?

**Condensed-matter justification** (Cosmic-Web): The Euclidean action minimum would provide a SECOND, independent mechanism for dump-point selection (in addition to the Turing/BCS mechanism chain). Independent confirmation strengthens the operating-point prediction.

**Pre-registered gate**: I_E(tau) + I_E^{one-loop}(tau) has a local minimum in [0.10, 0.30]. PASS if yes. FAIL if still monotone.

**Input**: Existing eigenvalue data, RPA-32b curvature.
**Output**: I_E(tau) profile with one-loop correction. Binary: minimum exists (YES/NO).

---

## 5. Updated Phonon-NCG Dictionary Entries

### Entry 1: Mode-Trapping Continuum (NEW)

| | v_group = 0 (Hawking Limit) | v_group = epsilon (Domain Wall Limit) |
|:--|:----------------------------|:--------------------------------------|
| **Mechanism** | Causal disconnection, trace over interior | Kinematic slowing, no trace |
| **Spectrum** | Thermal (Planckian) | Non-thermal (Parker) |
| **Back-reaction** | Destructive (evaporative) | Constructive (stabilizing, BCS) |
| **Information** | Exponentially scrambled | Algebraically determined |
| **Universality class** | Conformal (near-horizon geometry) | Topological (codimension of degeneracy) |
| **Framework realization** | Not realized (no causal horizon) | Domain wall van Hove enhancement |
| **Reference** | Paper 05 (Hawking 1975), Paper 12 (Unruh 1976) | W-32b, van Hove 1953 |
| **Status** | Structural parallel A. Joint conceptual result. |

### Entry 2: Nonlocal Vacuum Polarization (NEW)

| | Semiclassical Gravity | Spectral Action |
|:--|:----------------------|:----------------|
| **Local part** | Seeley-DeWitt / Euler-Heisenberg | Bare curvature (79.3% of chi = 20.43) |
| **Nonlocal part** | Bogoliubov-coefficient entanglement | Quantum metric (20.7% of chi = 20.43) |
| **Qualitative role** | Resolves information paradox (nonlocal correction to local thermal spectrum) | Circumvents Wall 4 (nonlocal correction to local Seeley-DeWitt monotonicity) |
| **Reference** | Paper 06 (Hawking 1976), Paper 14 (Penington 2019) | RPA-32b, Connes-QA Workshop Result 1 |
| **Status** | Structural parallel B. Mathematical identity for spectral action side (Connes-QA). |

### Entry 3: Horizon Continuum (NEW)

| | Semiclassical Gravity | Spectral Geometry |
|:--|:----------------------|:------------------|
| **v_group = 0** | Event horizon (Hawking, thermal) | Not realized in framework |
| **v_group = epsilon** | Kinematic barrier (quasi-thermal) | Domain wall (van Hove, non-thermal) |
| **Universality** | Conformal (near-horizon) | Topological (codimension of degeneracy) |
| **Reference** | Paper 05, Paper 12 | W-32b, van Hove 1953 |
| **Status** | Suggestive C. Proposed joint nomenclature. |

### Entry 4: Three-Term GSL (NEW)

| | Black Hole Thermodynamics | Domain Wall Condensation |
|:--|:--------------------------|:-------------------------|
| **Term 1** | Bekenstein-Hawking entropy decrease (-dA/4G) | Spectral entropy decrease (dS_spec < 0) |
| **Term 2** | Hawking radiation entropy (thermal) | Bogoliubov particle entropy (non-thermal, R = 1.5-3.7x) |
| **Term 3** | N/A (no condensation at BH horizon) | BCS condensate entropy (S = 0, pure state) |
| **GSL** | dS_BH + dS_rad >= 0 | dS_spec + dS_particles + dS_condensate >= 0 |
| **Reference** | Paper 11 (Bekenstein 1973) | Session 29a + this workshop |
| **Status** | Parallel B. Gate pre-registered for Session 33. |

---

## 6. Open Questions

### 6.1 Is the Domain Wall Thermodynamically Stable?

The free energy ratio Delta_F / T_eff ~ 0.5-2.0 places the wall in the MARGINAL stability regime. Cosmic-Web notes the 3He A-B interface is also marginally stable yet survives experimentally. Hawking notes the ratio is "not parametrically safe." The BCS gap equation (Priority 1) is decisive: if Delta_BCS > T_GH (wall effective temperature), the condensate survives. If not, the mechanism chain is self-defeating.

### 6.2 Does the One-Loop Corrected Euclidean Action Have a Minimum?

RPA-32b adds positive curvature at the dump point. The bare action is monotonically decreasing (H-1, Session 25). Whether the one-loop correction is large enough to create a local minimum in I_E(tau) determines whether the no-boundary proposal (Paper 09) independently selects the dump point. Priority 6 resolves this.

### 6.3 What Is the Domain Wall Volume Fraction?

Estimated f_wall ~ 0.01-0.1 from condensed-matter calibration, with Bekenstein upper bound. If f_wall < 0.01, the BCS mechanism is cosmologically irrelevant even if it works at individual walls. TURING-1 (Priority 2) is decisive.

### 6.4 Can the Domain Wall Carry Entropy?

If the van Hove trapping creates an effective causal barrier (modes with v_group -> 0 take effectively infinite time to cross), the wall carries area entropy in the Bekenstein-Hawking sense. The condensation transition (mixed -> pure state) then represents entropy decrease compensated by particle production. This connects to the island formula (Paper 14) and the identification of the domain wall as a quantum extremal surface. Theoretical framing, not a Session 33 computation.

### 6.5 Is the Information Content of the Frozen Modulus Unitary?

The frozen modulus (w = -1, Session 22d clock closure) encodes initial conditions (tau_initial, perturbation spectrum) in the BCS gap parameter Delta and the domain-wall pattern. Whether this encoding is unitary -- i.e., whether the final state uniquely determines the initial conditions -- determines whether there is an internal-space information paradox. If unitary, the condensation is a standard quantum process. If non-unitary, a resolution is needed analogous to the black hole information paradox.

### 6.6 Does the Superfluid Density Prediction Give Physical Masses?

Hawking's pre-registered prediction: rho_s(B2) = (2*Delta_BCS / V_cell) * 4.24. If BCS-at-walls yields Delta_BCS, this gives the London penetration depth and gauge boson mass at the wall. Whether the resulting mass scale connects to Standard Model masses is a Tier 3 question that depends on the full KK reduction.

---

## Self-Corrections During Workshop

### 1. Priority Ordering Reversal (Cosmic-Web)

Cosmic-Web initially ranked TURING-1 above wall-BCS on the grounds that the volume fraction is the ultimate cosmological discriminator. Hawking's sequential-logic argument ("first the mechanism, then the census") prevailed. Cosmic-Web conceded the BCS-first ordering while maintaining that TURING-1 is equally critical for the full chain.

### 2. Island Formula Downgraded from Gate to Target (Hawking)

Hawking initially proposed the island-formula bound as a Session 33 gate. Cosmic-Web's objection (requires G_eff in internal space, Channel 2 closed in Session 29) led to downgrading. The weaker form R >= 1 was adopted as the computable gate.

### 3. Passive-Dominant Classification Sharpened (Joint)

Initial discussion treated the active/passive distinction as a binary. Multi-round exchange refined it to a continuum parametrized by v_group (Result 1), with quantitative estimates: |beta|^2 ~ 0.01-0.05 (subdominant active component), van Hove enhancement 20-100x larger. The framework operates at v_group = epsilon, firmly in the passive regime.

---

## Summary Table: Workshop Results by Computation Status

| Result | New? | Computable? | Data Exists? | Session 33 Priority |
|:-------|:-----|:-----------|:-------------|:--------------------|
| Mode-trapping continuum (Result 1) | YES | Conceptual | N/A | N/A (framework) |
| Three-term GSL (Result 2) | YES | YES | YES | Priority 5 |
| Bogoliubov-Lindhard synthesis (Result 3) | YES | YES | YES | Priority 3 |
| Sound speed + wall temperature (Result 4) | YES | Partially | YES (c_eff); needs Delta_BCS | Contingent on P1 |
| Volume fraction + Bekenstein (Result 5) | YES | YES | Partial; needs TURING-1 | Priority 2 |
| Passive-dominant classification | REFINED | YES | YES | Priority 3 |
| Dump point self-consistency | CONVERGENT | Diagnostic | YES | N/A |
| Nonlocal vacuum polarization interpretation | CONVERGENT | N/A | N/A | N/A (interpretation) |

---

## Quantitative Estimates (Workshop-Derived)

| Quantity | Value | Source | Status |
|:---------|:------|:-------|:-------|
| |beta|^2 (Bogoliubov) | 0.01-0.05 | 3He A-B calibration | Estimate, needs extraction |
| c_eff (wall sound speed) | ~0.51 (spectral units) | g_B2/chi_bare ratio | Prediction, needs Bogoliubov dispersion |
| Delta_F / T_eff (thermal stability) | 0.5-2.0 | Joint estimate | Marginal, needs wall-BCS |
| f_wall (volume fraction) | 0.01-0.1 | 3He calibration + chi/D_B2 scaling | Estimate, needs TURING-1 |
| rho_s(B2) (superfluid density) | (2*Delta_BCS/V_cell) * 4.24 | Quantum metric identity | Pre-registered, needs Delta_BCS |

---

*Workshop synthesis by coordinator. All findings represent the joint output of multi-round adversarial exchange between hawking-theorist and cosmic-web-theorist, with self-corrections incorporated. The mode-trapping continuum (Result 1) and three-term GSL accounting (Result 2) are the workshop's primary conceptual contributions. The Bogoliubov-Lindhard synthesis (Result 3) and sound speed prediction (Result 4) are the primary computational contributions.*
