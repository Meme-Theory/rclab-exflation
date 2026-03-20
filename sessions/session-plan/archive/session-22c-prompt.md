# Session 22c: Non-Perturbative Channels — BCS Scan, Higgs-Sigma, Instantons, Cartan Flux

## Session Type: COMPUTATION + THEORETICAL ANALYSIS (hours-days)
## Agents: feynman-theorist + connes-ncg-theorist + landau-condensed-matter-theorist + coordinator
## Session Goal: Execute the highest-priority non-perturbative channel investigations that are independent of the coupled diagonalization (Session 22b). These mechanisms bypass the Dual Algebraic Trap by operating in mathematical sectors the trap cannot constrain.

---

# 0. OPERATIONAL RULES — READ BEFORE ANYTHING ELSE

## DEPENDENCY: RUNS AFTER SESSION 22b

This session depends on Session 22b results (block-diagonality theorem, retraction of inter-sector coupling). Read both 22a and 22b synthesis documents before beginning.

Read (required before starting):
- `sessions/session-22/session-22a-synthesis.md`
- `sessions/session-22/session-22b-synthesis.md`

## THREE-AGENT TEAM: STRICT MESSAGE DISCIPLINE

Three specialists + coordinator = risk of notification avalanche. Follow strictly:
- Maximum 3 messages per agent per hour
- Send each inter-agent message to ONE recipient, not all
- Coordinator routes findings to the full team; do not broadcast yourself

## TWO-PHASE STRUCTURE

**Phase A**: Each agent executes their assigned computations independently.
**Phase B**: Cross-pollination — identify connections between BCS result, Higgs-sigma result, and instanton result. These three mechanisms may interact.

**COMPLETION SIGNAL**: "SESSION 22c COMPLETE — all agents confirm."

## COMPUTATION ENVIRONMENT

**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s22c_`

---

# I. CONTEXT: THE NON-PERTURBATIVE FRONTIER

## Why Non-Perturbative Physics Is Required

From the Dual Algebraic Trap (Session 21c Theorem 1): all perturbative spectral mechanisms on SU(3) with standard SM embedding are algebraically closed. Two fixed ratios:
- **Trap 1 (spectral)**: F/B ~ 0.55 full-spectrum asymptotic ratio (Weyl's law, tau-independent, Session 20b). The fiber DOF ratio 16/44 = 4/11 ≈ 0.364 is a related but distinct quantity (fiber multiplicity vs full spectral weight).
- b_1/b_2 = 4/9 (Dynkin embedding index, representation-theoretically exact)

These traps apply to eigenvalue MAGNITUDES (spectral sums |lambda|^p, ln|lambda|). They do NOT apply to:
1. **BCS/Pomeranchuk condensates**: Operate on eigenvalue-flow matrix elements C_{nm}, not on eigenvalue magnitudes.
2. **Higgs-sigma portal**: The spectral action a_4 cross-coupling lambda_{H sigma} depends on quartic curvature/gauge combinations, not on the constant-ratio spectral sum.
3. **Instantons**: Non-analytic in the coupling — invisible to all finite-loop perturbation theory.
4. **Cartan flux**: The e^{-4tau} channel is algebraically confirmed (CP-1 = Trap 2) but the PHYSICAL observable connecting it to stabilization may not be S_signed.

## The Sign Paradox (Dirac, R2 Collab)

delta_T_total > 0 despite delta_T_b1 < 0 and delta_T_b2 < 0 throughout. The total is positive because the UV modes (p+q = 4,5,6, carrying 99.4% of signal) have ln(lambda^2) > 0; the leading minus sign maps negative × positive = positive total. The (0,0) singlet contributes Delta_b = 0 (gauge-neutral, no b-projection). This reveals:

- The traps and the physics live in ORTHOGONAL spectral sectors
- The gauge-charged sector (b1, b2) has the sign needed for a fixed point
- The gauge-neutral singlet overwhelms the gauge channels in the block-diagonal treatment
- Session 22b PROVED D_K is exactly block-diagonal (off-diagonal elements = 0.00e+00, eigenvalue match at 2.89e-15): coupled = block-diagonal identically. No inter-sector coupling exists.

The non-perturbative mechanisms in this session operate on the gauge-charged sector directly, potentially bypassing the singlet's dominance.

---

# II. REQUIRED READING

## ALL agents (MANDATORY):

1. **R2 master collab**: `sessions/session-21/session-21c-r2-master-collab.md`
   — Section VI (new physics from R2: VI.2 Landau at d=8, VI.3 envelope reinterpretation). Section VIII Tier 1 (items 3-8: BCS channel scan, Higgs-sigma, order-one condition, instanton, Berry curvature, bowtie fine structure).

2. **Session 21c synthesis**: `sessions/session-21/session-21c-phase0-synthesis.md`
   — Section III (structural theorems: Dual Algebraic Trap), Section IV (CP-4 condensate persistence dichotomy), Section VII (per-agent critical questions).

3. **Session 22a synthesis**: `sessions/session-22/session-22a-synthesis.md`

4. **Session 22b synthesis**: `sessions/session-22/session-22b-synthesis.md`
   — Section II (block-diagonality theorem: C_{nm} = 0 identically between sectors), Section IV (retraction of Session 21b coupling estimate), Section X (corrected Kosmann norms).

5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:------------------|
| feynman | R2 Feynman collab (`session-21c-r2-feynman-collab.md`). Session 21a A-2 (self-consistency map), BCS gap equation mapping. `researchers/Feynman/09_1972_Statistical_Mechanics_A_Set_of_Lectures.md` (path integral / BCS analogy). |
| connes | R2 Connes collab (`session-21c-r2-connes-collab.md`). `researchers/Connes/13_2012_Connes_Chamseddine_Mukhanov_Sigma_field.md` — sigma field and Higgs-sigma portal. Connes Paper 07 (spectral action). |
| landau | R2 Landau collab (`session-21c-r2-landau-collab.md`). `researchers/Landau/08_1950_Ginzburg_Landau_superconductivity.md` and `researchers/Landau/03_1935_Landau_diamagnetism.md`. Session 21a A-3 (phase transition classification). |

---

# III. PHASE A: COMPUTATION ASSIGNMENTS

| Agent | Primary Computation | Secondary |
|:------|:-------------------|:----------|
| feynman | F-1: Pomeranchuk stability / BCS channel scan | F-2: Instanton action S_inst(tau) on Jensen SU(3) |
| connes | C-1: Higgs-sigma portal lambda_{H,sigma}(tau) | C-2: Order-one condition [[D,a], JbJ^{-1}] = 0 vs tau |
| landau | L-1: Landau free energy classification on tau-line | L-2: BCS-BEC crossover tau from g*N(0) |
| coordinator | Tracks progress, routes cross-domain connections |

---

### Computation F-1: Pomeranchuk Stability / BCS Channel Scan

**Primary**: feynman-theorist
**Priority**: HIGHEST (Landau's top priority from R2, "decisive test")
**Runtime**: 1-4 hours

**Background**: The BCS condensate requires TWO ingredients:
1. A Fermi surface (or gap-edge) with sufficient density of states
2. An ATTRACTIVE effective interaction in at least one channel

The coupled diagonalization (22b) provides ingredient 1. This computation tests ingredient 2: does an attractive pairing channel exist in the Dirac spectrum of (SU(3), g_Jensen)?

**The Pomeranchuk criterion**: A Fermi liquid state is unstable toward condensation in channel with angular momentum l if:

```
F_l^s < -(2l+1)
```

where F_l^s is the Landau parameter. In the KK context, replace the Fermi liquid channels with SU(3) representation channels (p,q). The analog: the effective interaction in channel (p,q) is attractive if the sector eigenvalue DECREASES as tau increases (softening).

**The BCS gap equation** in the KK context:

```
Delta_n = Sum_m V_{nm}^{eff}(tau) * Delta_m / (2 * sqrt(xi_m^2 + |Delta_m|^2))
```

where V_{nm}^{eff} is the effective intra-sector interaction, xi_m = lambda_m - lambda_F (quasiparticle energy relative to gap edge), and Delta is the condensate order parameter.

**CRITICAL NOTE (from 22b)**: The inter-sector coupling matrix C_{nm} = 0 identically (block-diagonality theorem). The BCS pairing interaction must therefore arise from INTRA-SECTOR physics: either (a) the eigenvalue response to tau deformation within a single (p,q) sector (tested in step 1 below), (b) instanton-mediated interactions (tested in F-2), or (c) Higgs-sigma portal coupling (tested in C-1). Do NOT use inter-sector matrix elements — they are zero.

**The question**: Does the intra-sector eigenvalue response to tau produce an effective ATTRACTIVE interaction in any channel? The sign of the effective attraction comes from whether the gap equation has a non-trivial solution Delta > 0.

**Protocol (BCS channel scan)**:

1. **Softening analysis** (using existing eigenvalue data): For each sector (p,q) at each tau, compute the derivative d(lambda_min(p,q))/dtau. Sectors with d(lambda_min)/dtau < 0 are "softening" (becoming lighter), which is the analog of an attractive channel.
   - Data: `tier0-computation/s19a_sweep_data.npz`
   - Identify all sectors where dE/dtau < 0 at any tau in [0.15, 0.35]

2. **BCS threshold estimate** (using intra-sector Kosmann correction): From Session 22b (corrected):
   - The Session 21b "4-5x inter-sector coupling" is RETRACTED — it measured ||L_{e_a} g|| (geometric tensor norm), not inter-sector D_K matrix elements (which are identically zero by block-diagonality).
   - Intra-sector Kosmann correction: ||K_a^{correct}|| = 1.41-1.76 (Session 22b PA-2 Proof 2)
   - **CAVEAT**: ||K_a|| is a Dirac operator correction norm within each sector, NOT directly a pairing interaction in the BCS sense. Using it as g_eff is an order-of-magnitude estimate whose physical interpretation requires care. A more principled effective interaction would be d^2 E/d tau^2 (eigenvalue curvature as an effective spring constant).
   - BCS critical coupling g_c = lambda_min(tau) / (N(0) * V_K)
   - With N(0) = number of gap-edge eigenvalues (see note below): g_c ~ lambda_min(0.30) / N(0)
   - Rough estimate: g_eff/g_c ~ O(1-4), but this is an ORDER-OF-MAGNITUDE estimate, not a precision calculation.

3. **Gap equation linearization**: Expand Delta around zero. The gap equation has non-trivial solution if the largest eigenvalue of V_{nm}^{eff}/(2 lambda_m) exceeds 1. Use the intra-sector eigenvalue response (d lambda/d tau) to construct V_{nm}^{eff} within each sector.

4. **22b established C_{nm} = 0 identically between sectors** — skip inter-sector coupling computation. The Pomeranchuk criterion must be evaluated using intra-sector effective interactions only.

**Pre-registered Constraint Gates** (Landau R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | BCS gap equation has non-trivial solution at tau in [0.15, 0.35] (condensate exists) | 20 | +8-12 pp |
| COMPELLING | Attractive channel identified (at least one sector softens monotonically in physical window) | 8 | +4-6 pp |
| INTERESTING | Pomeranchuk instability in one sector at tau > 0.40 (outside FR minimum) | 3 | +1-2 pp |
| CLOSED | No attractive channel in any sector, gap equation only trivial solution everywhere | 0.2 | -5-8 pp |

Note on condensate + DESI tension (CP-4, Session 21c): If condensate forms (Branch A), w = -1 (DESI-incompatible UNLESS disrupted during early universe evolution). Report honestly. Do not assume the condensate is DESI-compatible without computing the thermal disruption.

**Script**: `tier0-computation/s22c_bcs_channel_scan.py`
**Output**: `tier0-computation/s22c_bcs_channel_scan.npz`, `tier0-computation/s22c_bcs_channel_scan.txt`

---

### Computation F-2: Instanton Action S_inst(tau) on Jensen SU(3)

**Primary**: feynman-theorist
**Priority**: High (SP + Feynman + QA from R1, SP Tier 1 item 5)
**Runtime**: 1-4 hours (requires Yang-Mills instanton ansatz)

**Background**: From Session 21b B-2, instanton channels were partially assessed:
- 4D gauge instantons: S_inst = 8pi^2|k|/g_YM^2, tau-INDEPENDENT (volume-preserving closes dS/dtau)
- Internal YM instantons: S_inst increases with tau (same direction as V_CW) — CLOSED
- Gravitational instantons: I_E ~ -R_K * Vol, MARGINAL

**New from Berry (R2 collab, Novel Proposal #13)**: Stokes phenomenon at monopole transitions. The WKB (instanton) approximation undergoes qualitative changes at the Berry curvature monopoles M0, M1, M2. At a monopole, the WKB connection formulas change sign (Stokes phenomenon). This means:
- dS_inst/dtau could flip sign at M1 or M2
- The instanton action that was increasing could start decreasing inside the (0,0)-gap phase [0.15, 1.55]

**Protocol (gravitational + Stokes)**:

1. **Gravitational instanton**: I_E(tau) = -R_K(tau) * Vol(K) / (16 pi G)
   - Load R_K(tau) from existing curvature data or `sp2_final_verification.py`
   - Compute I_E at 21 tau values
   - Compute dI_E/dtau. Sign convention: the Euclidean path integral weight is exp(-I_E). Lower I_E = MORE probable configuration. Therefore dI_E/dtau > 0 means finite tau is PREFERRED (tau=0 has lower action = higher weight, but larger tau has EVEN lower action). dI_E/dtau < 0 means tau=0 is preferred.

2. **Stokes phenomenon at monopoles**:
   - The instanton action on the deformed manifold can be computed from the 2-form associated with the self-dual connection. For the Jensen deformation, the Hodge star is tau-dependent.
   - The key is whether the self-duality equation F = *F has solutions that change character at the monopole locations.
   - Analytic estimate: near M1 (tau~0.15), the metric changes from (1,0)/(0,1)-dominated gap to (0,0)-dominated gap. The Hodge dual of a 2-form changes significantly because the volume element depends on sector.
   - Estimate: does dS_inst/dtau flip sign at tau = tau_M1?

3. **If Stokes flip is present**: This would make the instanton a non-perturbative mechanism that naturally selects the (0,0)-gap phase. Pre-registered: if sign flip of dS_inst/dtau at tau_M1 in [0.10, 0.20] => NEW FINDING, +5-8 pp.

**Pre-registered Constraint Gates** (SP + Feynman R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | dI_E/dtau > 0 in [0.15, 0.55] AND Stokes flip at M1 | 20 | +8-12 pp |
| COMPELLING | dI_E/dtau > 0 in physical window (tau > 0.15 Euclidean-preferred) | 8 | +4-6 pp |
| INTERESTING | Stokes flip identified even if magnitude small | 3 | +2-3 pp |
| CLOSED | I_E monotonically decreasing throughout (tau=0 always preferred) | 0.3 | -3-4 pp |

**Script**: `tier0-computation/s22c_instanton_action.py`
**Output**: `tier0-computation/s22c_instanton_action.npz`, `tier0-computation/s22c_instanton_action.txt`

---

### Computation C-1: Higgs-Sigma Portal lambda_{H,sigma}(tau)

**Primary**: connes-ncg-theorist
**Priority**: HIGH (Connes' top NCG priority from R2, "the only untested NCG-native mechanism")
**Runtime**: 1-2 hours (analytic + a_4 coefficient extraction)

**Background**: From Session 21c, Connes (R2 collab) elevated the Higgs-sigma portal as the single most important untested NCG mechanism:

"The Higgs-sigma cross-coupling lambda_{H,sigma}(tau) from the spectral action's a_4 coefficient is NOT a spectral sum — it depends on quartic curvature/gauge-field combinations that are independent of the constant-ratio trap."

The spectral action's a_4 Seeley-DeWitt coefficient contains cross-terms of the form:

```
a_4[D^2] ~ integral [R_K^2 + |Ric|^2 + |F|^2 * R_K + |F|^4 + ... + cross terms]
```

The cross-coupling between the Higgs field H and the sigma field (Jensen modulus) appears as:

```
lambda_{H,sigma}(tau) = d^2 a_4/d(sigma^2) d(H^2)|_{tau}
```

This is the coefficient of the |H|^2 |sigma|^2 coupling in the effective potential. If lambda_{H,sigma} has the right sign and magnitude, the combined potential V(H, sigma) selects tau even when V_eff(tau) alone does not — because the Higgs VEV provides an additional tachyonic contribution.

**Connection to Connes 13**: The sigma field paper (Connes-Chamseddine-Mukhanov 2012) shows the sigma field corrects the Higgs mass from 170 to 125 GeV through a similar portal mechanism. The same structure applies to the Jensen modulus.

**Protocol**:

1. **Compute a_4(tau)** (already done in part in Session 20a):
   - Load `sd20a_seeley_dewitt_gate.py` — the a_4 computation from Session 20a.
   - Extend it to compute the cross-derivative d^2 a_4/(d sigma^2 d H^2).
   - The sigma field here is the Jensen modulus tau; d/d sigma = d/d tau for the quadratic terms.

2. **The coupling formula** (attributed to Connes Paper 07, Section III — **PI: VERIFY THIS CITATION AND FORMULA BEFORE RUNNING; Sonnet-generated, not independently checked**):
   ```
   lambda_{H,sigma}(tau) = (f_0/4) * (d^2/d tau^2) * integral |E_{tau}|^2 dvol
   ```
   where E_{tau} is the tau-dependent part of the connection curvature (the gauge field on the internal space). If this formula cannot be verified, derive lambda_{H,sigma} from the a_4 cross-derivative in step 1 directly.

3. **Compute at all 21 tau values**. Plot lambda_{H,sigma}(tau) vs tau.

4. **Key question**: Is lambda_{H,sigma} negative anywhere in [0.15, 0.40]?
   - If lambda_{H,sigma} < 0: the portal is tachyonic in that direction. The Higgs VEV <H>^2 = v^2 drives tau toward the minimum of lambda_{H,sigma} * v^2. This selects a preferred tau WITHOUT requiring a minimum in V_eff(tau) alone.
   - If lambda_{H,sigma} > 0: the portal stabilizes the Higgs but does not select tau.
   - If lambda_{H,sigma} < 0 at tau in [0.20, 0.35]: this is the Weinberg angle window. The Higgs VEV then dynamically stabilizes the modulus at the physical value.

**Pre-registered Constraint Gates** (Connes R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | lambda_{H,sigma} < 0 at tau in [0.20, 0.35] with |lambda_{H,sigma}| * v^2 > |V_eff'(tau_0)| | 30 | +12-18 pp |
| COMPELLING | lambda_{H,sigma} < 0 at some tau in [0.10, 0.50] | 12 | +6-10 pp |
| INTERESTING | lambda_{H,sigma} non-monotonic (changes sign at some tau) | 4 | +2-4 pp |
| CLOSED | lambda_{H,sigma} > 0 everywhere (portal stabilizes Higgs only, does not select tau) | 0.3 | -2-3 pp |

**Note on independence from spectral sums**: The key property of this mechanism is that it operates on the PRODUCT structure of the spectral triple (H_F cross SU(3)), not on the KK spectral sum alone. The Dual Algebraic Trap applies to spectral sums over (p,q) sectors. The Higgs-sigma portal comes from the finite part of the spectral triple (H_F, J_F, D_F), which is NOT trapped. This is why Connes identifies it as the only remaining NCG-native perturbative escape.

**Script**: `tier0-computation/s22c_higgs_sigma.py`
**Output**: `tier0-computation/s22c_higgs_sigma.npz`, `tier0-computation/s22c_higgs_sigma.png`

---

### Computation C-2: Order-One Condition [[D,a], JbJ^{-1}] = 0 vs tau

**Primary**: connes-ncg-theorist
**Priority**: Medium (Connes + Baptista proposal, R1 Novel Physics III.8)
**Runtime**: 1-2 hours (algebraic)

**Background**: The NCG axiom system for spectral triples includes the first-order condition:
[[D, a], JbJ^{-1}] = 0 for all a, b in A

On the finite algebra A_F, this is automatically satisfied by construction (Barrett's classification). But on the FULL algebra A = C(M4) tensor A_F, deforming the internal geometry (tau) may violate this condition for tau outside a bounded interval [0, tau_max].

**If this is correct**: The spectral triple (A, H, D_K(tau)) FAILS TO EXIST as a valid NCG spectral triple for tau > tau_max. The Jensen deformation is algebraically restricted to [0, tau_max]. The modulus is stabilized by the AXIOMS of NCG geometry, not by a potential minimum.

**Protocol**:

1. **Set up the commutator**: For the specific algebra A_F and Dirac operator D_K(tau), compute [[D_K(tau), a_F], J_F b_F J_F^{-1}] for a sample of elements (a_F, b_F) in A_F.

2. **Compute the norm**: ||[[D_K(tau), a_F], J_F b_F J_F^{-1}||^2 as a function of tau.

3. **At tau=0 (round metric)**: this norm should vanish by symmetry.
   At tau > 0: compute whether the norm grows with tau or remains bounded.

4. **Identify tau_max**: if the norm diverges or exceeds a threshold at some tau_max, this is the algebraic bound.

5. **Expected tau_max**: The first-order condition is related to the bimodule structure of the connection on the C^2 coset. From Baptista Paper 18, the L_tilde correction (vs L_X) describes a different operator (Lie derivative on sections vs covariant derivative). Whether this connects to the NCG order-one condition is an UNTESTED CONJECTURE — no computation or paper establishes this link. The C-2 computation should proceed without assuming this connection.

**Pre-registered Constraint Gates** (Connes + Baptista R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| DECISIVE | ||[[D,a], JbJ^{-1}]|| = 0 for tau in [0, tau_max] with tau_max in [0.30, 0.40] | 40 | +15-20 pp |
| COMPELLING | tau_max exists and is in [0.20, 0.60] | 15 | +8-12 pp |
| INTERESTING | tau_max exists but is in [1.0, 2.0] (too large to constrain physical window) | 3 | +1-2 pp |
| CLOSED | Order-one condition satisfied for all tau in [0, 2.0] (no algebraic constraint) | 0.5 | -1 pp |
| NEUTRAL | Condition violated for all tau > 0 (condition is too strong — framework broken at level 0) | 0.1 | -15 pp |

Note: NEUTRAL is listed for completeness. If the order-one condition fails even at small tau, there is a fundamental inconsistency in the framework that precedes all the stabilization questions.

**Script**: `tier0-computation/s22c_order_one.py`
**Output**: `tier0-computation/s22c_order_one.txt`

---

### Computation L-1: Landau Free Energy Classification on the tau-Line

**Primary**: landau-condensed-matter-theorist
**Priority**: Medium (map convexity structure for first-order transition characterization)
**Runtime**: 1-2 hours (using existing V_total data)

**Background**: From Session 21a, Landau identified the Ginzburg criterion and cubic term V'''(0) = -7.2. The complete Landau free energy classification requires:
1. Identifying all convexity changes in V_eff(tau)
2. Locating the spinodal point (where V'' changes sign)
3. Computing the Ginzburg number G_i = (fluctuation contribution) / (mean-field contribution)
4. Determining whether the transition is first-order and computing the barrier height

From Session 21a (post-synthesis, Landau): V''_total > 0 everywhere. The FULL V_total has no spinodal. But V_IR (low-mode only) may have a spinodal even if V_total does not.

**New context from Session 21c / R2**: Landau (R2) established that d = 8 (internal space dimension) > d_uc = 4 (upper critical dimension for standard phi^4 Landau-Ginzburg theory). For phi^4-type transitions, this means mean-field theory is EXACT for the internal space degrees of freedom. However: (1) d_uc may differ for other universality classes, and (2) the modulus dynamics effectively live in d_eff = 1. Reconciling these two dimensionality arguments is the key theoretical task.

**Protocol**:

1. **From existing V_total data** (`l20_vtotal_minimum.npz`):
   - Compute V'(tau), V''(tau), V'''(tau) via numerical differentiation.
   - Locate zero of V'': tau_spinodal where V'' = 0 (if it exists).
   - If V'' > 0 everywhere (confirmed in Session 21a): report this. No spinodal in full perturbative potential.

2. **From V_IR data** (`s21c_V_IR.npz`):
   - Compute V_IR'(tau), V_IR''(tau).
   - Does V_IR'' change sign? At what tau?
   - This would be the spinodal of the IR sector, even if absent in V_total.

3. **Ginzburg number**:
   ```
   G_i = (k_B T_c)^2 / (c_s a * xi_0^d_eff)
   ```
   where T_c is the transition temperature, c_s is specific heat jump, xi_0 is correlation length, d_eff = 1. For our context: T_c ~ the barrier height, xi_0 ~ the coherence length in tau-space. Estimate from the available V_eff data. G_i >> 1 means strong fluctuations dominate.

4. **He-3/He-4 analog calibration**:
   - He-4 lambda transition: G_i ~ 0.3, weakly fluctuating, mean-field plus logarithmic corrections.
   - He-3 A-phase: G_i ~ 1, strongly fluctuating.
   - Our modulus: G_i = ?
   - If G_i >> 1: perturbative V_eff is unreliable by Landau's criterion, not just approximate.

5. **First-order transition characterization** (using V'''(0) = -7.2 from V_total, Session 21a Landau analysis — note: V_total has V'' > 0 everywhere, so the cubic term alone does not produce a spinodal in the full potential; the first-order transition, if it exists, requires a non-perturbative barrier):
   - From Landau theory: the first-order transition temperature T_1 = T_0 - V'''^2 / (6V^{(4)}) where T_0 is the mean-field transition temperature.
   - Estimate the barrier height from V'''(0) and V^{(4)}(0) (the quartic term from numerical differentiation).
   - The latent heat L = T_1 * delta S at the transition. Is L large enough to produce a detectable gravitational wave signal?

**Pre-registered Constraint Gates** (Landau R2 collab):

| Tier | Criterion | BF | Prob shift |
|:-----|:----------|:---|:-----------|
| COMPELLING | V_IR'' < 0 at some tau in [0.10, 0.40] (IR spinodal exists) | 8 | +4-6 pp |
| INTERESTING | G_i > 10 (perturbative V_eff unreliable, but mean-field not exact for modulus) | 3 | +1-2 pp |
| NEUTRAL | V_total'' > 0 throughout (confirmed from 21a) | 1 | 0 pp |
| CLOSED | G_i < 1 AND V_IR'' > 0 everywhere (mean-field exact, no spinodal anywhere) | 0.4 | -2 pp |

**Script**: `tier0-computation/s22c_landau_classification.py`
**Output**: `tier0-computation/s22c_landau_classification.npz`, `tier0-computation/s22c_landau_classification.txt`

---

### Computation L-2: BCS-BEC Crossover Line g*N(0) vs tau

**Primary**: landau-condensed-matter-theorist
**Priority**: Medium (Tesla + QA R1 proposal, now more urgent after delta_T result)
**Runtime**: 30 minutes

**Background**: Tesla (R1 collab) computed that g*N(0) ~ 8-10 in the singlet window, placing the system deep in the BEC regime (not BCS weak-coupling). This is important for two reasons:

1. **BEC condensates are qualitatively MORE robust** than BCS condensates: they do not require a Fermi surface singularity, they are stable against thermal disruption, and they persist to strong coupling.

2. **The BCS-BEC crossover** occurs around g*N(0) ~ 1. Above 1: BEC (molecular condensate). Below 1: BCS (Cooper pairs). The crossover tau should be identifiable from the spectrum.

**Data source**: `tier0-computation/s19a_sweep_data.npz`

**Protocol**:

1. For each tau in [0.10, 1.00]:
   - Extract N(0) = number of eigenvalues at the gap edge (i.e., eigenvalue degeneracy, NOT total modes in sector — the (0,0) sector has 16 spinor-component modes total, but only ~2 eigenvalues sit at the gap edge in the singlet window; outside the singlet window, ~24 eigenvalues cluster at the gap edge). Cross-check against 22b mode counts.
   - From Session 22b (corrected): intra-sector Kosmann correction ||K_a|| ~ 1.41-1.76 at tau=0.15-0.30 (NOT the retracted 4-5x inter-sector estimate). Use this range as the coupling estimate; tau-dependence of ||K_a|| within the physical window is not yet derived, so treat 1.41-1.76 as the uncertainty band.
   - Compute g*N(0)(tau)

2. Find tau_crossover where g*N(0) = 1 (BCS-BEC crossover). Is tau_crossover inside or outside the physical window [0.15, 1.55]?

3. **For tau in [0.15, 0.55] (FR minimum region)**: If g*N(0) >> 1, the condensate at the FR minimum is BEC-type (molecular), not BCS (Cooper pair). This changes the stabilization physics:
   - BEC: modulus locked by molecular condensate, w = -1 exactly
   - BCS: gap equation solution, more fragile, w may deviate from -1

4. **Pre-registered** (Tesla/QA R1): if g*N(0) > 5 at tau = 0.30 → BEC confirmed → condensate is non-perturbatively robust → Branch A (w=-1) is strongly favored.

**Output**: Append to `s22c_landau_classification.txt` (a few lines)

---

# IV. PHASE B: CROSS-POLLINATION SYNTHESIS

After Phase A computations complete:

## Cross-Pollination Seed Questions

**feynman -> connes**: "The BCS attractive channel scan — does the pairing interaction couple to the gauge-charged sector (b1, b2 contributions) or to the gauge-neutral singlet? If it couples to gauge-charged modes, the Higgs-sigma portal (your computation) would modulate the coupling strength. Is there an algebraic link?"

**connes -> landau**: "The Higgs-sigma portal lambda_{H,sigma}(tau) — does it couple to the sigma field that enters the Ginzburg-Landau theory? Specifically: does lambda_{H,sigma} < 0 (attractive) at the same tau where V_IR'' < 0 (spinodal exists)? If both are negative at the same tau, that tau is selected by TWO independent mechanisms."

**landau -> feynman**: "The BCS-BEC crossover at g*N(0) = 1 — if the system is deep BEC (g*N(0) ~ 8-10), the first-order Landau transition (V'''(0) = -7.2) and the BEC condensate could be different faces of the same physics. In He-3, the BEC regime corresponds to the strong-coupling A-phase. Does the condensate formation at the FR minimum match the He-3 A-phase analog?"

**All -> coordinator**: "Three mechanisms (BCS attractive pairing, Higgs-sigma portal, instanton Stokes flip) — are they independent, or does one REQUIRE the others? Specifically: if the instanton action decreases inside [0.15, 1.55] (Stokes flip), does this provide the attractive interaction that the BCS channel needs?"

## Required Synthesis Content

The coordinator assembles `sessions/session-22/session-22c-synthesis.md` containing:

1. **Phase A results table**: Each computation, result, Constraint Gate verdict, probability shift.
2. **Mechanism independence**: Are the three mechanisms (BCS, Higgs-sigma, instanton) algebraically independent? Can more than one apply simultaneously?
3. **Combined scenario**: If BCS attractive + Higgs-sigma negative + instanton Stokes flip: combined probability shift (must be less than sum to avoid double-counting).
4. **Condensate character**: BEC or BCS? Implications for w(z) and DESI.
5. **Updated probability**: Per-agent + panel consensus.
6. **Handoff to 22d**: What do these results imply for the rolling modulus ODE?

---

# V. OUTPUT FILES

## Primary output:

`sessions/session-22/session-22c-synthesis.md`

## Computation output files:

| File | Content |
|:-----|:--------|
| `s22c_bcs_channel_scan.py/npz/txt` | BCS Pomeranchuk scan |
| `s22c_instanton_action.py/npz/txt` | Instanton action + Stokes |
| `s22c_higgs_sigma.py/npz/png` | Higgs-sigma portal |
| `s22c_order_one.py/txt` | Order-one condition |
| `s22c_landau_classification.py/npz/txt` | Landau classification |

---

# VI. THE SAGAN STANDARD

All gates above are pre-registered before computation runs. The specific failure mode to guard against: discovering that "the Higgs-sigma portal has lambda_{H sigma} < 0" and immediately claiming this "solves" the stabilization problem. It does not. It provides ONE piece of evidence that a non-perturbative mechanism EXISTS. It does not compute that mechanism quantitatively. Report what was computed, not what was implied.

The BCS channel scan is the clearest test: either the gap equation has a non-trivial solution at the FR minimum or it does not. This is binary. Report it binary.

---

*"The perturbative spectral program is a closed book. What remains is a precisely defined non-perturbative problem."*
*— Session 21c Closing Assessment*
